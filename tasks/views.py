from django.http import HttpResponse
from django.urls import reverse


def index(request):
    # Получаем URL для главной страницы quality_control
    quality_control_index_url = reverse('quality_control:index')

    # Получаем URL для другой страницы tasks
    another_page_url = reverse('tasks:another_page')

    # Формируем HTML с обеими ссылками
    html = f"<h1>Страница приложения tasks</h1><a href='{quality_control_index_url}'>Ссылка на главную страницу quality_control</a> <a href='{another_page_url}'>Ссылка на другую страницу</a>"
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")
