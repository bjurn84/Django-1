# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    html_content = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Здесь вы найдете информацию о моем сайте.</p>
    </body>
    </html>
    """
    logger.info("Пользователь посетил главную страницу")
    return HttpResponse(html_content)

def about_me(request):
    html_content = """
    <html>
    <head><title>О себе</title></head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Меня зовут Павел, и это мой первый Django-сайт.</p>
        <p>Здесь вы найдете информацию обо мне и моих увлечениях.</p>
    </body>
    </html>
    """
    logger.info("Пользователь посетил страницу 'О себе'")
    return HttpResponse(html_content)