from django.shortcuts import render
from django.views.generic import View, DetailView
from django.http import HttpResponse, JsonResponse
from club_project.models import TblProjectIntroduction, TblClub
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import jwt
import json


@method_decorator(csrf_exempt, name='dispatch')
class ProjectCV(View):
    template_name = 'club/project_create.html'
    # token = .decode('utf-8')


    def post(self, request, club_id):
        if request.META["CONTENT_TYPE"] == "application/json":
            request = json.loads(request.body)
            project = TblProjectIntroduction()
            project.club = TblClub.objects.get(id=club_id)
            project.title = request["title"]
            project.contents = request["contents"]
            project.started_at = request["started_at"]
            project.ended_at = request["ended_at"]
            project.save()
            return HttpResponse(status=201)
        # else:
        #     project = TblProjectIntroduction()
        #     project.club = 1
        #     project.title = request.POST["title"]
        #     project.contents = request.POST["contents"]
        #     project.started_at = request.POST["started_at"]
        #     project.ended_at = request.POST["started_at"]
        #     project.save()
        #     return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ProjectDV(View):

    def get(self, request, club_id, project_id):
        project = TblProjectIntroduction.objects.get(id=project_id, club_id=club_id)
        data = {
            'title': project.title,
            'contents': project.contents,
            'created_at': project.created_at,
            'ended_at': project.updated_at,
            'started_at': project.started_at,
            'ended_at': project.ended_at,
        }
        return JsonResponse(data, status=200)

    def put(self, request, club_id, project_id):
        project = TblProjectIntroduction.objects.get(id=project_id, club_id=club_id)
        if request.META["CONTENT_TYPE"] == "application/json":
            request = json.loads(request.body)
            project.club = TblClub.objects.get(id=club_id)
            project.title = request["title"]
            project.contents = request["contents"]
            project.started_at = request["started_at"]
            project.ended_at = request["ended_at"]
            project.save()
            return HttpResponse(status=201)

    def delete(self, request, club_id, project_id):
        project = TblProjectIntroduction.objects.get(id=project_id, club_id=club_id)
        project.delete()
        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateClubIntro(View):

    def put(self, request, club_id):
        club = TblClub.objects.get(id=club_id)
        if request.META["CONTENT_TYPE"] == "application/json":
            request = json.loads(request.body)
            club.contents = request["contents"]
            club.save()
            return HttpResponse(status=200)