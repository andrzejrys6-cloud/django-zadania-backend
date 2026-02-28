from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    """Strona główna - lista opublikowanych postów."""
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    """Szczegóły pojedynczego posta."""
    post = get_object_or_404(Post, id=post_id, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_posts(request, category_id):
    """Lista postów w danej kategorii."""
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category, published=True)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})
