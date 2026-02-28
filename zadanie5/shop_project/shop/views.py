from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.db import transaction
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from .serializers import (
    ProductSerializer, CategorySerializer,
    CartSerializer, CartItemSerializer,
    OrderSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_permissions(self):
        """Tylko admin może tworzyć/edytować/usuwać produkty."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        """Filtrowanie produktów przez parametry URL."""
        queryset = Product.objects.all()

        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        search = self.request.query_params.get('search')

        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class CartViewSet(viewsets.GenericViewSet):
    """Koszyk - każdy użytkownik ma jeden koszyk."""
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_or_create_cart(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def list(self, request):
        """Pobierz zawartość koszyka."""
        cart = self.get_or_create_cart()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='items')
    def add_item(self, request):
        """Dodaj produkt do koszyka."""
        cart = self.get_or_create_cart()
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Produkt nie istnieje'}, status=404)

        if product.stock < quantity:
            return Response({'error': 'Niewystarczający stan magazynowy'}, status=400)

        # Jeśli produkt już w koszyku - zwiększ ilość
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return Response(CartItemSerializer(item).data, status=201)

    @action(detail=False, methods=['delete'], url_path='items/(?P<item_id>[^/.]+)')
    def remove_item(self, request, item_id=None):
        """Usuń produkt z koszyka."""
        cart = self.get_or_create_cart()
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({'error': 'Nie znaleziono produktu w koszyku'}, status=404)
        item.delete()
        return Response(status=204)


class OrderViewSet(viewsets.GenericViewSet):
    """Zamówienia użytkownika."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def list(self, request):
        """Lista zamówień zalogowanego użytkownika."""
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Szczegóły zamówienia."""
        try:
            order = Order.objects.get(id=pk, user=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Nie znaleziono zamówienia'}, status=404)
        return Response(OrderSerializer(order).data)

    def create(self, request):
        """Złóż zamówienie z zawartości koszyka."""
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': 'Koszyk jest pusty'}, status=400)

        items = cart.items.all()
        if not items:
            return Response({'error': 'Koszyk jest pusty'}, status=400)

        # Transakcja - albo wszystko się uda, albo nic
        with transaction.atomic():
            total = sum(item.product.price * item.quantity for item in items)
            order = Order.objects.create(user=request.user, total_price=total)

            for item in items:
                if item.product.stock < item.quantity:
                    raise Exception(f'Brak towaru: {item.product.name}')
                # Zmniejszenie stanu magazynowego
                item.product.stock -= item.quantity
                item.product.save()
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Opróżnienie koszyka po zamówieniu
            items.delete()

        return Response(OrderSerializer(order).data, status=201)

    @action(detail=True, methods=['patch'], url_path='status', permission_classes=[IsAdminUser])
    def update_status(self, request, pk=None):
        """Zmiana statusu zamówienia - tylko admin."""
        try:
            order = Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Nie znaleziono zamówienia'}, status=404)

        new_status = request.data.get('status')
        valid_statuses = ['pending', 'paid', 'shipped', 'delivered']
        if new_status not in valid_statuses:
            return Response({'error': f'Nieprawidłowy status. Wybierz z: {valid_statuses}'}, status=400)

        order.status = new_status
        order.save()
        return Response(OrderSerializer(order).data)
