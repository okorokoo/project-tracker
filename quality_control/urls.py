from django.urls import path, include
from quality_control import views
from tasks.views import TaskDetailView, ProjectDetailView

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>/bugs/<int:bug_id>/update', views.BugUpdateView.as_view(), name='update_bug'),
    path('project/<int:project_id>/bugs/<int:bug_id>/update', views.update_bug, name='update_bug'),
    path('project/<int:project_id>/features/<int:feature_id>/update', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('project/<int:project_id>/features/<int:feature_id>/update', views.update_feature, name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug_report'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug_report'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature_request'),
    path('features/<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature_request'),
    path('project/<int:project_id>/bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('project/<int:project_id>/features/new/', views.create_feature_request, name='create_feature_request'),
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