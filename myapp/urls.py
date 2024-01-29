# myapp/urls.py
from django.urls import path
from .views import home, about_me

urlpatterns = [
    path('', home, name='home'),
    path('about-me/', about_me, name='about_me'),
]