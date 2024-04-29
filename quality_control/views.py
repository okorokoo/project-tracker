from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views import View
from django.views.generic import DetailView, ListView

from .models import BugReport, FeatureRequest
from tasks.models import Project

from .forms import BugReportForm, FeatureRequestForm


def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})


def create_bug_report(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = BugReportForm(request.POST or None, initial={'project_id': None})
        if form.is_valid():
            bug = form.save(commit=False)
            bug.project = project
            bug.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm(initial={'project_id': project.id})

    return render(request, 'quality_control/bug_report_form.html', {'form': form, 'project': project})


def create_feature_request(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = FeatureRequestForm(request.POST or None, initial={'project_id': None})
        if form.is_valid():
            feature = form.save(commit=False)
            feature.project = project
            feature.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm(initial={'project_id': project.id})

    return render(request, 'quality_control/feature_request_form.html', {'form': form, 'project': project})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_detail.html'
    context_object_name = 'bug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        task = bug.task
        project = bug.project
        return render(request, 'quality_control/bug_report_detail.html', {'bug': bug, 'task': task, 'project': project})


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        task = feature.task
        project = feature.project
        return render(request, 'quality_control/feature_detail.html', {'feature': feature, 'task': task, 'project': project})
