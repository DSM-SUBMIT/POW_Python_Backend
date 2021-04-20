from django.urls import path
from club_project import views

app_name = 'club'

urlpatterns = [
    path('club/<int:club_id>/project', views.ProjectListAPIView.as_view()),
    path('club/<int:club_id>/project/<int:project_id>', views.ProjectDetailAPIView.as_view()),
    path('club/<int:club_id>', views.ClubIntroUpdateAPIView.as_view(), name='update_club_intro'),
]