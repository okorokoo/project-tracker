from django.urls import path, include
from quality_control import views
from tasks.views import TaskDetailView, ProjectDetailView

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', include([
        path('', views.bug_list, name='bug_list'),
        path('<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
        path('<int:bug_id>/tasks/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
        path('<int:bug_id>/projects/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    ])),
    path('features/', include([
        path('', views.feature_list, name='feature_list'),
        path('<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'),
        path('<int:feature_id>/tasks/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
        path('<int:feature_id>/projects/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    ]))
]