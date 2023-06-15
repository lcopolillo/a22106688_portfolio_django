from django.shortcuts import render

from .models import Post

def home_page_view(request):
    return render(request, 'portfolio/index.html')

def blog_page_view(request):
    return render(request, 'portfolio/blog.html')

def post_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'posts/posts.html', context)