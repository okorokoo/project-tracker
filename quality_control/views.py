from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .models import BugReport, FeatureRequest


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a> <a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> Status: {bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def bug_detail(request, bug_id):
    html = f"<h1>Детали бага {bug_id}</h1>"
    return HttpResponse(html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список улучшений</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> Status: {feature.status}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def feature_id_detail(request, feature_id):
    html = f"<h1>Детали улучшения {feature_id}</h1>"
    return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a> <a href='{feature_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        task = bug.task
        project = bug.project
        response_html = f'<h1>{bug.title}</h1><p>Description: {bug.description}</p><p>Status: {bug.status}</p><p>Priority: {bug.priority}</p>'
        response_html += '<h2>Задача</h2>'
        response_html += f'<a href="tasks/{task.id}/">{task.name}</a>'
        response_html += '<h2>Проект</h2>'
        response_html += f'<a href="projects/{project.id}/">{project.name}</a>'
        return HttpResponse(response_html)


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        task = feature.task
        project = feature.project
        response_html = f'<h1>{feature.title}</h1><p>Description: {feature.description}</p><p>Status: {feature.status}</p><p>Priority: {feature.priority}</p>'
        response_html += '<h2>Задача</h2>'
        response_html += f'<a href="tasks/{task.id}/">{task.name}</a>'
        response_html += '<h2>Проект</h2>'
        response_html += f'<a href="projects/{project.id}/">{project.name}</a>'
        return HttpResponse(response_html)