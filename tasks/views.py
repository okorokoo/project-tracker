from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

from .models import Project, Task

from .forms import FeedbackForm, ProjectForm, TaskForm


def index(request):
    return render(request, 'tasks/index.html')


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_create.html', {'form': form})


def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')


class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'


class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project

        return context


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['info@example.com']
            recipients.append(email)

            send_mail(subject, message, email, recipients)

            return redirect('/tasks')
    else:
        form = FeedbackForm()
    return render(request, 'tasks/feedback.html', {'form': form})
