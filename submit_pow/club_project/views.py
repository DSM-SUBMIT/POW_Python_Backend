from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from club_project import serializers
from club_project.models import TblProjectIntroduction, TblClub

from submit_pow import settings

import jwt


class ProjectListAPIView(APIView):

    serializer_class = serializers.ProjectSerializer

    def get(self, request, club_id):
        serializer = self.serializer_class(TblProjectIntroduction.objects.filter(club_id=club_id), many=True)
        return Response(serializer.data)

    def post(self, request, club_id):
        """Create a project object"""
        token = jwt.decode(request.auth, settings.SECRET_KEY, algorithms=["HS256"])
        # {'user_id': 1, 'username': 'kwak', 'exp': 1619447947, 'email': 'kwak@kwak.com', 'orig_iat': 1618843147}
        if token['club_id'] != club_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        request.data['club_id'] = club_id
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ProjectDetailAPIView(APIView):

    serializer_class = serializers.ProjectSerializer

    # noinspection PyMethodMayBeStatic
    def get_object(self, project_id):
        return get_object_or_404(TblProjectIntroduction, pk=project_id)

    def get(self, request, club_id, project_id, format=None):
        """Project detail"""
        project = self.get_object(project_id)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def put(self, request, club_id, project_id):
        """Update a project object"""
        project = self.get_object(project_id)
        request.data['club_id'] = club_id
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, project_id):
        """Delete a project object"""
        project = self.get_object(project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClubIntroUpdateAPIView(APIView):

    def put(self, request, club_id):
        """Update a club introduction(contents)"""
        club = get_object_or_404(TblClub.objects.filter(id=club_id))
        serializer = serializers.ClubSerializer(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

