from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CategoryViewSet

# Router automatycznie tworzy wszystkie endpointy CRUD
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Endpoint do logowania w przeglądarce (panel DRF)
    path('api-auth/', include('rest_framework.urls')),
]
