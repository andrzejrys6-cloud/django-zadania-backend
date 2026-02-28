# Zadania Django

Pięć zadań z Django od podstaw do zaawansowanych.

---

## Wymagania

- Python 3.10 lub nowszy — pobierz z https://python.org/downloads  
  Podczas instalacji zaznacz **"Add Python to PATH"**

---

## Instalacja (tylko raz)

Otwórz terminal w folderze `django_zadania/` i wpisz:

```powershell
py -m pip install -r requirements.txt
```

Poczekaj aż wszystko się pobierze i zainstaluje.

---

## Uruchamianie zadań

Każde zadanie to osobny projekt Django. Schemat jest zawsze taki sam — wejdź do folderu projektu i wykonaj trzy komendy:

```powershell
# Przykład dla zadania 1:
cd zadanie1/blog_project

# Krok 1 — utwórz tabele w bazie danych (tylko przy pierwszym uruchomieniu)
py manage.py makemigrations
py manage.py migrate

# Krok 2 — utwórz konto administratora (tylko przy pierwszym uruchomieniu)
py manage.py createsuperuser

# Krok 3 — uruchom serwer
py manage.py runserver
```

Podczas `createsuperuser` terminal zapyta o nazwę użytkownika, email i hasło — wpisz co chcesz, to będzie Twoje konto do panelu admina.

Następnie otwórz w przeglądarce:
- Aplikacja: **http://127.0.0.1:8000**
- Panel admina: **http://127.0.0.1:8000/admin**

Zatrzymanie serwera: **CTRL+C**

> Zadanie 5 ma inną nazwę folderu projektu: `cd zadanie5/shop_project`

---

## Opis zadań

| Folder     | Zadanie                                         | Poziom              |
|------------|-------------------------------------------------|---------------------|
| zadanie1/  | Blog — modele i panel admina                    | Podstawowy          |
| zadanie2/  | Blog — widoki i strony HTML z Bootstrap         | Podstawowy/Średni   |
| zadanie3/  | Blog — REST API (Django REST Framework)         | Średni              |
| zadanie4/  | Blog — rejestracja, logowanie, profile, avatary | Średni/Zaawansowany |
| zadanie5/  | Sklep — produkty, koszyk, zamówienia            | Zaawansowany        |

Każdy folder ma swój własny README z dokładnym opisem jak używać danego zadania.

---

## Przydatne komendy Django

```powershell
# Po zmianie czegokolwiek w models.py — wygeneruj migrację i zastosuj ją
py manage.py makemigrations
py manage.py migrate

# Uruchom serwer na innym porcie jeśli 8000 jest zajęty
py manage.py runserver 8001
```
