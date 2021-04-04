from django.db import models

class Project(models.Model):
    # id = models.ForeignKey()
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    started_at = models.DateField(blank=True)
    ended_at = models.DateField(blank=True)

    class Meta:
        db_table = "tbl_project_introduction"
