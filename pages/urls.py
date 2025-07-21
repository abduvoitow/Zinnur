# pages/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from pages.forms import CustomLoginForm  
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
