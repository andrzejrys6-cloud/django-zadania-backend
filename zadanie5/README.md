# Zadanie 5 — Sklep e-commerce: API

Backend sklepu internetowego. Produkty, koszyk, zamówienia — wszystko przez REST API. Brak interfejsu HTML, obsługa przez przeglądarkowy panel DRF.

---

## Jak uruchomić

```powershell
cd zadanie5/shop_project
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

---

## Jak używać

Otwórz: **http://127.0.0.1:8000/api/**

Kliknij **Log in** w prawym górnym rogu i zaloguj się danymi z `createsuperuser`.

---

## Ścieżka użytkownika (krok po kroku)

### Krok 1 — Dodaj kategorie (jako admin)
Wejdź na **http://127.0.0.1:8000/api/categories/** i dodaj kategorie np. "Elektronika", "Odzież".

### Krok 2 — Dodaj produkty (jako admin)
Wejdź na **http://127.0.0.1:8000/api/products/** i dodaj produkty.

```json
{
  "name": "Laptop Dell XPS",
  "description": "Wydajny laptop",
  "price": "4999.99",
  "stock": 10,
  "category": 1
}
```

### Krok 3 — Dodaj produkt do koszyka
Wejdź na **http://127.0.0.1:8000/api/cart/add_item/** i wyślij:

```json
{
  "product_id": 1,
  "quantity": 2
}
```

### Krok 4 — Sprawdź koszyk
Wejdź na **http://127.0.0.1:8000/api/cart/** — zobaczysz zawartość swojego koszyka z cenami.

### Krok 5 — Złóż zamówienie
Wejdź na **http://127.0.0.1:8000/api/orders/** i kliknij **POST** (bez żadnych danych).  
Zamówienie powstaje automatycznie z zawartości koszyka. Koszyk zostaje opróżniony, stan magazynowy produktów zmniejszony.

### Krok 6 — Historia zamówień
**http://127.0.0.1:8000/api/orders/** — lista Twoich zamówień z cenami i statusami.

---

## Endpointy

### Produkty

| Metoda | Adres | Co robi | Kto może |
|--------|-------|---------|----------|
| GET | /api/products/ | Lista produktów (z filtrowaniem) | Wszyscy |
| POST | /api/products/ | Dodaj produkt | Tylko admin |
| PUT | /api/products/1/ | Zaktualizuj produkt | Tylko admin |
| DELETE | /api/products/1/ | Usuń produkt | Tylko admin |

### Filtrowanie produktów

Możesz filtrować listę produktów przez parametry w adresie URL:

```
/api/products/?category=Elektronika
/api/products/?min_price=1000&max_price=5000
/api/products/?search=laptop
/api/products/?category=Elektronika&min_price=1000&search=dell
```

### Koszyk

| Metoda | Adres | Co robi |
|--------|-------|---------|
| GET | /api/cart/ | Pokaż koszyk |
| POST | /api/cart/add_item/ | Dodaj produkt do koszyka |
| DELETE | /api/cart/remove_item/1/ | Usuń pozycję z koszyka |

### Zamówienia

| Metoda | Adres | Co robi | Kto może |
|--------|-------|---------|----------|
| GET | /api/orders/ | Lista moich zamówień | Zalogowany użytkownik |
| POST | /api/orders/ | Złóż zamówienie z koszyka | Zalogowany użytkownik |
| GET | /api/orders/1/ | Szczegóły zamówienia | Zalogowany użytkownik |
| PATCH | /api/orders/1/update_status/ | Zmień status zamówienia | Tylko admin |

### Statusy zamówień (dla admina)

```json
{ "status": "pending" }    ← oczekujące
{ "status": "paid" }       ← opłacone
{ "status": "shipped" }    ← wysłane
{ "status": "delivered" }  ← dostarczone
```

---

## Panel admina

**http://127.0.0.1:8000/admin** — podgląd wszystkich danych w bazie: produkty, koszyki, zamówienia, użytkownicy.

---

## Struktura projektu

```
zadanie5/shop_project/
├── manage.py
├── shop_project/
│   ├── settings.py
│   └── urls.py
└── shop/
    ├── models.py          ← Product, Category, Cart, CartItem, Order, OrderItem
    ├── serializers.py     ← zamiana danych na JSON
    ├── views.py           ← cała logika: koszyk, zamówienia, walidacja stanu magazynowego
    └── admin.py
```
