from django.db import models


class TblClub(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(unique=True, max_length=6)
    password = models.CharField(max_length=60)
    profile_path = models.CharField(max_length=255, blank=True, null=True)
    banner_path = models.CharField(max_length=255, blank=True, null=True)
    contents = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_club'


class TblClubTag(models.Model):
    tag = models.ForeignKey('TblTag', models.DO_NOTHING)
    club_id = models.ForeignKey(TblClub, models.DO_NOTHING, db_column='club_id')

    class Meta:
        managed = False
        db_table = 'tbl_club_tag'
        unique_together = (('id', 'tag', 'club_id'),)


class TblProjectIntroduction(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    club_id = models.ForeignKey(TblClub, models.DO_NOTHING, db_column='club_id')

    class Meta:
        managed = False
        db_table = 'tbl_project_introduction'
        unique_together = (('id', 'club_id'),)


class TblProjectIntroductionImage(models.Model):
    path = models.CharField(max_length=255)
    project_introduction = models.ForeignKey(TblProjectIntroduction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_project_introduction_image'
        unique_together = (('id', 'project_introduction'),)


class TblTag(models.Model):
    tag_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_tag'
