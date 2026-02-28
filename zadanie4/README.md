# Zadanie 4 — Blog: rejestracja, logowanie, profile

Blog z pełnym systemem kont użytkowników. Każdy może się zarejestrować, zalogować, napisać posta i edytować swój profil z avatarem.

---

## Jak uruchomić

```powershell
cd zadanie4/blog_project
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

---

## Jak używać

Otwórz: **http://127.0.0.1:8000**

---

## Ścieżka zwykłego użytkownika

### 1. Zarejestruj konto
Kliknij **Rejestracja** w prawym górnym rogu nawigacji.  
Wpisz nazwę użytkownika i hasło dwa razy. Formularz sam sprawdzi czy hasło jest wystarczająco silne.

### 2. Zaloguj się
Po rejestracji zostaniesz zalogowany automatycznie.  
Następnym razem kliknij **Zaloguj** i podaj swoje dane.

### 3. Napisz posta
Kliknij **Nowy post** w nawigacji.  
Wypełnij tytuł i treść. Zaznacz **Opublikowany** jeśli chcesz żeby był widoczny dla innych.

### 4. Edytuj profil
Kliknij **Profil** w nawigacji.  
Możesz dodać krótki opis (bio) i wgrać zdjęcie profilowe (avatar).

### 5. Moje posty
Kliknij **Moje posty** — zobaczysz listę wszystkich swoich postów z informacją czy są opublikowane czy nie.  
Kliknij **Edytuj** przy dowolnym poście żeby go zmienić.

---

## Ważne zasady

- Każdy użytkownik widzi tylko przycisk **Edytuj** przy swoich postach — nie może edytować cudzych
- Posty z odznaczonym "Opublikowany" są widoczne tylko dla autora na liście "Moje posty"
- Avatar musi być plikiem graficznym (jpg, png)

---

## Panel admina

**http://127.0.0.1:8000/admin** — zaloguj się danymi z `createsuperuser`.  
Admin widzi i może edytować wszystko — wszystkich użytkowników, wszystkie posty, wszystkie profile.

---

## Struktura projektu

```
zadanie4/blog_project/
├── manage.py
├── blog_project/
│   ├── settings.py
│   └── urls.py
├── blog/
│   ├── models.py          ← Post (powiązany z User), Profile, Category
│   ├── views.py           ← rejestracja, profil, tworzenie/edycja postów
│   ├── forms.py           ← formularze dla profilu i posta
│   └── admin.py
└── templates/
    ├── blog/              ← szablony stron
    └── registration/      ← szablony logowania i rejestracji
```
