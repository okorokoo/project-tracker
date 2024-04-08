from django.urls import path, include
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', include([
        path('', views.bug_list, name='bug_list'),
        path('<int:bug_id>/', views.bug_detail, name='bug_detail'),
    ])),
    path('features/', include([
        path('', views.feature_list, name='feature_list'),
        path('<int:feature_id>', views.feature_id_detail, name='feature_id_detail'),
    ]))
]