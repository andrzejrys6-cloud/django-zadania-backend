from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Rozszerzenie wbudowanego modelu User o dodatkowe dane."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'Profil: {self.user.username}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Teraz autor to użytkownik, nie string
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
