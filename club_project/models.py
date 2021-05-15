from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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
