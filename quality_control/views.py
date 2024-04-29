from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView

from .models import BugReport, FeatureRequest
from tasks.models import Project

from .forms import BugReportForm, FeatureRequestForm


def index(request):
    return render(request, 'quality_control/index.html')


class IndexView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})


class BugReportListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'


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


def bug_detail(request, bug_id):
	bug = get_object_or_404(BugReport, id=bug_id)
	task = bug.task
	project = bug.project

	return render(request, 'quality_control/bug_detail.html', {'bug': bug, 'task': task, 'project': project})


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        task = feature.task
        project = feature.project
        return render(request, 'quality_control/feature_detail.html', {'feature': feature, 'task': task, 'project': project})


def feature_detail(request, feature_id):
	feature = get_object_or_404(FeatureRequest, id=feature_id)
	task = feature.task
	project = feature.project

	return render(request, 'quality_control/feature_detail.html', {'feature': feature, 'task': task, 'project': project})


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'


    def form_valid(self, form):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(pk=project_id)
        form.instance.project = project

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('quality_control:bug_list')


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'

    def form_valid(self, form):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(pk=project_id)
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quality_control:feature_list')


def update_bug(request, project_id, bug_id):
    project = get_object_or_404(Project, pk=project_id)
    bug = get_object_or_404(BugReport, pk=bug_id)

    if request.method == 'POST':
        form = BugReportForm(request.POST or None, initial={'project_id': None}, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(initial={'project_id': project.id}, instance=bug)

    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


class BugUpdateView(UpdateView):
	model = BugReport
	form_class = BugReportForm
	template_name = 'quality_control/bug_update.html'
	pk_url_kwarg = 'bug_id'

	def get_success_url(self):
		return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})


def update_feature(request, project_id, feature_id):
    project = get_object_or_404(Project, pk=project_id)
    feature = get_object_or_404(FeatureRequest, pk=feature_id)

    if request.method == 'POST':
        form = FeatureRequestForm(request.POST or None, initial={'project_id': None}, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_id_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(initial={'project_id': project.id}, instance=feature)

    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


class FeatureUpdateView(UpdateView):
	model = FeatureRequest
	form_class = FeatureRequestForm
	template_name = 'quality_control/feature_update.html'
	pk_url_kwarg = 'feature_id'

	def get_success_url(self):
		return reverse_lazy('quality_control:feature_id_detail', kwargs={'feature_id': self.object.id})


def delete_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()

    return redirect('quality_control:bug_list')


class BugDeleteView(DeleteView):
	model = BugReport
	pk_url_kwarg = 'bug_id'
	success_url = reverse_lazy('quality_control:bug_list')
	template_name = 'quality_control/bug_confirm_delete.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['bug'] = self.object

		return context


def delete_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()

    return redirect('quality_control:feature_list')

class FeatureDeleteView(DeleteView):
	model = FeatureRequest
	pk_url_kwarg = 'feature_id'
	success_url = reverse_lazy('quality_control:feature_list')
	template_name = 'quality_control/feature_confirm_delete.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['feature'] = self.object

		return context
