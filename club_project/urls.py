from django.urls import path
from club_project import views

app_name = 'club'

urlpatterns = [

    # club/1
    path('<int:club_id>', views.club_update, name='club'),

    # club/1
    path('<int:club_id>/project', views.post_list, name='project'),

    # club/1/project/1
    path('<int:club_id>/project/<int:project_id>', views.ProjectDetailView.as_view(), name='project_detail'),
]
