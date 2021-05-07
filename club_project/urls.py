from django.urls import path
from club_project import views

app_name = 'club'

urlpatterns = [

    # club/1
    path('<int:club_id>', views.ClubAPIView.as_view(), name='club'),

    # club/1/project
    path('<int:club_id>/project', views.ProjectAPIView.as_view(), name='project'),

    # club/1/project/1
    path('<int:club_id>/project/<int:project_id>', views.ProjectDetailAPIView.as_view(), name='project_detail'),
]