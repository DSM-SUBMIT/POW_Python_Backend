from django.contrib import admin
from club_project.models import TblProjectIntroduction

@admin.register(TblProjectIntroduction)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contents', 'started_at', 'ended_at')
