from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('index/', views.home_page_view, name='index'),
]
