from django.urls import path
from club_project.views import *

app_name = 'club'

urlpatterns = [
    path('', ProjectCV.as_view()),
    path('project/<int:pk>/', ProjectDV.as_view()),
]