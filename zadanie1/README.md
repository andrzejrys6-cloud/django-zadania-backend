# Zadanie 1 — Blog: modele i panel admina

Prosta aplikacja blogowa. Nie ma żadnego interfejsu dla zwykłych użytkowników — całość obsługuje się przez wbudowany panel admina Django.

---

## Jak uruchomić

```powershell
cd zadanie1/blog_project
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Podczas `createsuperuser` terminal zapyta Cię o nazwę użytkownika, email i hasło — wpisz co chcesz, to Twoje konto admina.

---

## Jak używać

Otwórz panel admina: **http://127.0.0.1:8000/admin**

Zaloguj się danymi które podałeś przy `createsuperuser`.

### Co możesz robić w panelu

**Kategorie** — dodaj kilka kategorii np. "Technologia", "Sport", "Kultura"

**Posty** — dodaj post, wypełnij:
- Tytuł
- Treść
- Autor (wpisz dowolne imię)
- Opublikowany — zaznacz jeśli chcesz żeby był widoczny
- Kategorie — wybierz jedną lub więcej z listy

### Przydatne funkcje panelu
- Kolumna **Opublikowany** na liście postów — możesz klikać bezpośrednio żeby zmieniać bez wchodzenia do posta
- Filtr po prawej stronie — filtruj posty po statusie lub kategorii
- Wyszukiwarka — szuka po tytule, autorze i treści

---

## Struktura projektu

```
zadanie1/blog_project/
├── manage.py              ← stąd uruchamiasz komendy
├── blog_project/
│   ├── settings.py        ← konfiguracja projektu
│   └── urls.py            ← główne adresy URL
└── blog/
    ├── models.py          ← definicja tabel w bazie (Post, Category)
    └── admin.py           ← konfiguracja panelu admina
```
