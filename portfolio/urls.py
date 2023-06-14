from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('blog/', views.blog_page_view, name='blog'),
]
