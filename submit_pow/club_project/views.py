from django.shortcuts import render
from django.views.generic import View, DetailView
from django.http import JsonResponse, HttpResponse
from club_project.models import Project

class ProjectCV(DetailView):
    def post(self):
        return


class ProjectDV(DetailView):
    model = Project
    template_name = 'club/project_detail.html'






