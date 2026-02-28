from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('register/', views.register, name='register'),
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/nowy/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edytuj/', views.post_edit, name='post_edit'),
    path('profil/', views.profile, name='profile'),
    path('moje-posty/', views.my_posts, name='my_posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
