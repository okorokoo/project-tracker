from django.forms import ModelForm
from .models import BugReport, FeatureRequest
from tasks.models import Task


class BugReportForm(ModelForm):

    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('initial', {}).get('project_id')
        super().__init__(*args, **kwargs)
        print(project_id)
        if project_id:
            self.fields['task'].queryset = Task.objects.filter(project_id=project_id)

    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'task']


class FeatureRequestForm(ModelForm):

    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('initial', {}).get('project_id')
        super().__init__(*args, **kwargs)
        print(project_id)
        if project_id:
            self.fields['task'].queryset = Task.objects.filter(project_id=project_id)

    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'task']
