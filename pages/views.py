from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
    

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    """Display all published posts with category filtering"""
    posts = Post.objects.filter(status='published')
    
    # Filter by category if category_slug is provided
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """Display single post detail"""
    post = get_object_or_404(Post, slug=slug, status='published')
    
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)