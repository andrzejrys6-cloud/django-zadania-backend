# Zadanie 2 — Blog: widoki i szablony HTML

Rozbudowa zadania 1 o publiczne strony dostępne dla każdego — lista postów, szczegóły posta, posty w kategorii.

---

## Jak uruchomić

```powershell
cd zadanie2/blog_project
py manage.py makemigrations blog
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

---

## Jak używać

### Jako administrator — dodawanie treści

1. Wejdź na **http://127.0.0.1:8000/admin**
2. Dodaj kilka kategorii
3. Dodaj kilka postów — pamiętaj żeby zaznaczyć **Opublikowany**, inaczej nie pojawią się na stronie

### Jako zwykły użytkownik — przeglądanie bloga

| Adres | Co pokazuje |
|-------|-------------|
| http://127.0.0.1:8000/ | Lista wszystkich opublikowanych postów |
| http://127.0.0.1:8000/post/1/ | Szczegóły posta o ID 1 |
| http://127.0.0.1:8000/category/1/ | Wszystkie posty w kategorii o ID 1 |

Na stronie głównej każdy post ma klikalne etykiety kategorii — kliknięcie przenosi do listy postów z tej kategorii.

---

## Struktura projektu

```
zadanie2/blog_project/
├── manage.py
├── blog_project/
│   ├── settings.py
│   └── urls.py            ← adresy URL całego projektu
└── blog/
    ├── models.py
    ├── views.py           ← logika każdej strony
    ├── urls.py            ← adresy URL aplikacji blog
    └── admin.py
templates/blog/
    ├── base.html          ← wspólny szablon z nawigacją
    ├── post_list.html     ← strona główna
    ├── post_detail.html   ← szczegóły posta
    └── category_posts.html
```
