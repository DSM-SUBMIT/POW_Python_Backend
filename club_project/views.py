from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from club_project import serializers
from club_project.models import TblProjectIntroduction, TblClub

from submit_pow import settings

import jwt


def verify_auth_token(request):
    auth = request.headers['Authorization']
    token = auth.replace('Bearer ', '')
    token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return token['club_id']

def return_401_or_403(res_club_id, club_id):
    if not res_club_id:
        return Response(
                {"error_message": "인증 실패"},
                status=status.HTTP_401_UNAUTHORIZED
            )
    elif res_club_id != club_id:
        return Response(
            {"error_message": "권한 없음"},
            status=status.HTTP_403_FORBIDDEN
        )
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectAPIView(APIView):
    """동아리별로 프로젝트를 보거나 생성"""
    serializer_class = serializers.ProjectSerializer

    def get(self, request, club_id):
        queryset = TblProjectIntroduction.objects.filter(club_id=club_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, club_id):
        """Create a project object"""
        res_club_id = verify_auth_token(request)
        if not res_club_id or res_club_id != club_id:
            return return_401_or_403(res_club_id, club_id)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ProjectDetailAPIView(APIView):

    serializer_class = serializers.ProjectSerializer

    @staticmethod
    def get_object(club_id, project_id):
        return get_object_or_404(TblProjectIntroduction, pk=project_id, club_id=club_id)

    def get(self, request, club_id, project_id):
        """Project detail"""
        project = self.get_object(club_id, project_id)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def put(self, request, club_id, project_id):
        """Update project"""
        res_club_id = verify_auth_token(request)
        if not res_club_id or res_club_id != club_id:
            return return_401_or_403(res_club_id, club_id)

        project = self.get_object(club_id, project_id)
        serializer = self.serializer_class(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, club_id, project_id):
        """Delete a project object"""
        res_club_id = verify_auth_token(request)
        if not res_club_id or res_club_id != club_id:
            return return_401_or_403(res_club_id, club_id)

        project = self.get_object(club_id, project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClubAPIView(APIView):

    serializer_class = serializers.ClubSerializer

    def put(self, request, club_id):
        """Update a club introduction(contents)"""
        res_club_id = verify_auth_token(request)
        if not res_club_id or res_club_id != club_id:
            return return_401_or_403(res_club_id, club_id)

        club = get_object_or_404(TblClub.objects.filter(id=club_id))
        club.contents = request.data['contents']
        club.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
