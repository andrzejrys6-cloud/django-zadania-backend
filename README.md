# Zadania Django

Pięć zadań z Django od podstaw do zaawansowanych.

---

## Wymagania

- Python 3.10 lub nowszy — pobierz z https://python.org/downloads  
  Podczas instalacji zaznacz **"Add Python to PATH"**
- Git — pobierz z https://git-scm.com/downloads

---

## Instalacja (tylko raz)

Otwórz terminal w folderze `django_zadania/` i wpisz:

```powershell
py -m pip install -r requirements.txt
```

---

## Uruchamianie zadań

Każde zadanie to osobny projekt. Schemat jest zawsze taki sam:

```powershell
# Wejdź do folderu zadania (przykład dla zadania 1)
cd zadanie1/blog_project

# Utwórz tabele w bazie danych (tylko przy pierwszym uruchomieniu)
py manage.py migrate

# Utwórz konto administratora (tylko przy pierwszym uruchomieniu)
py manage.py createsuperuser

# Uruchom serwer
py manage.py runserver
```

Następnie otwórz: **http://127.0.0.1:8000**  
Panel admina: **http://127.0.0.1:8000/admin**

Zatrzymanie serwera: **CTRL+C**

> Zadanie 5 ma inną nazwę folderu projektu — `cd zadanie5/shop_project`

---

## Opis zadań

| Folder    | Zadanie                                         | Poziom              |
|-----------|-------------------------------------------------|---------------------|
| zadanie1/ | Blog — modele i panel admina                    | Podstawowy          |
| zadanie2/ | Blog — widoki i szablony HTML                   | Podstawowy/Średni   |
| zadanie3/ | Blog — REST API (Django REST Framework)         | Średni              |
| zadanie4/ | Blog — rejestracja, logowanie, profile, avatary | Średni/Zaawansowany |
| zadanie5/ | Sklep e-commerce — produkty, koszyk, zamówienia | Zaawansowany        |

---

## Przydatne komendy Django

```powershell
# Po zmianie czegokolwiek w models.py — wygeneruj migrację
py manage.py makemigrations

# Zastosuj migracje do bazy danych
py manage.py migrate

# Utwórz konto admina
py manage.py createsuperuser

# Uruchom serwer na innym porcie (jeśli 8000 jest zajęty)
py manage.py runserver 8001
```

---

## Jak wrzucić na GitHuba

### Krok 1 — Skonfiguruj Git (tylko raz)
```powershell
git config --global user.name "TwojeImie"
git config --global user.email "twoj@email.com"
```

### Krok 2 — Utwórz repozytorium na GitHubie
1. Wejdź na https://github.com
2. Kliknij zielony przycisk **New**
3. Wpisz nazwę np. `django-zadania`
4. Wybierz **Public** lub **Private**
5. **NIE zaznaczaj** "Add a README file"
6. Kliknij **Create repository**

### Krok 3 — Wyślij kod
W terminalu w folderze `django_zadania/`:

```powershell
git init
git add .
git commit -m "Zadania Django"
git branch -M main
git remote add origin https://github.com/TWOJA_NAZWA/django-zadania.git
git push -u origin main
```

### Krok 4 — Przy kolejnych zmianach
```powershell
git add .
git commit -m "Co zmieniłem"
git push
```
