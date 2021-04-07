from django.urls import path
from club_project.views import *

app_name = 'club'

urlpatterns = [
    path('project/', ProjectCV.as_view(), name='create_project'),
    path('project/<int:project_id>/', ProjectDV.as_view(), name='detail_project'),
    path('', UpdateClubIntro.as_view(), name='update_club_intro'),
]