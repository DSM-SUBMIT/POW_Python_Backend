from rest_framework import serializers

from club_project import models


class ProjectSerializer(serializers.ModelSerializer):
    """Serializes a project object"""

    class Meta:
        model = models.TblProjectIntroduction
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    """Serializes a club object"""

    class Meta:
        model = models.TblClub
        fields = '__all__'
