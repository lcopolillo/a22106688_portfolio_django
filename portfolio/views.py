from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/index.html')

def blog_page_view(request):
    return render(request, 'portfolio/blog.html')
