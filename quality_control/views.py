from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a> <a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("Список отчётов об ошибках")


def bug_detail(request, bug_id):
    html = f"<h1>Детали бага {bug_id}</h1>"
    return HttpResponse(html)


def feature_list(request):
    return HttpResponse("Список запросов на улучшение")


def feature_id_detail(request, feature_id):
    html = f"<h1>Детали улучшения {feature_id}</h1>"
    return HttpResponse(html)
