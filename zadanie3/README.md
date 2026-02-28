# Zadanie 3 — Blog: REST API

Blog z interfejsem API zamiast stron HTML. Zamiast przeglądać posty w przeglądarce, pobierasz je jako JSON — tak jak robi to np. aplikacja mobilna.

---

## Jak uruchomić

```powershell
cd zadanie3/blog_project
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

---

## Jak używać

Otwórz przeglądarkowy interfejs API: **http://127.0.0.1:8000/api/**

Django REST Framework daje Ci od razu ładny interfejs gdzie możesz przeglądać i testować endpointy bez żadnych dodatkowych narzędzi.

---

## Endpointy

### Posty

| Metoda | Adres | Co robi | Kto może |
|--------|-------|---------|----------|
| GET | /api/posts/ | Lista wszystkich postów | Wszyscy |
| POST | /api/posts/ | Dodaj nowy post | Tylko zalogowani |
| GET | /api/posts/1/ | Szczegóły posta o ID 1 | Wszyscy |
| PUT | /api/posts/1/ | Zaktualizuj post | Tylko zalogowani |
| DELETE | /api/posts/1/ | Usuń post | Tylko zalogowani |

### Kategorie

| Metoda | Adres | Co robi |
|--------|-------|---------|
| GET | /api/categories/ | Lista kategorii |
| POST | /api/categories/ | Dodaj kategorię |

---

## Jak się zalogować w interfejsie

W prawym górnym rogu strony **http://127.0.0.1:8000/api/** kliknij **Log in** i podaj dane z `createsuperuser`. Po zalogowaniu możesz używać POST, PUT, DELETE.

---

## Jak dodać post przez API

Na stronie **http://127.0.0.1:8000/api/posts/** po zalogowaniu przewiń na dół — zobaczysz formularz. Wypełnij pola i kliknij **POST**.

Albo wyślij JSON:
```json
{
  "title": "Mój post",
  "content": "Treść posta",
  "author": "Jan",
  "published": true,
  "category_ids": [1]
}
```

---

## Struktura projektu

```
zadanie3/blog_project/
├── manage.py
├── blog_project/
│   ├── settings.py
│   └── urls.py
└── blog/
    ├── models.py
    ├── serializers.py     ← zamienia obiekty Python na JSON i z powrotem
    ├── views.py           ← ViewSets obsługujące każdy endpoint
    └── admin.py
```
