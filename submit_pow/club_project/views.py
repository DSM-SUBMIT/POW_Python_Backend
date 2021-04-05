from django.shortcuts import render
from django.views.generic import View, DetailView
from django.http import JsonResponse, HttpResponse
from club_project.models import TblProjectIntroduction

class ProjectCV(View):
    def post(self, request):
        project = TblProjectIntroduction()
        project.title = request.title
        project.contents = request.content



class ProjectDV(DetailView):
    model = TblProjectIntroduction
    template_name = 'club/project_detail.html'


