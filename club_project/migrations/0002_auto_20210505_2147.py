# Generated by Django 3.2 on 2021-05-05 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tblclub',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tblclubtag',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tblprojectintroduction',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tblprojectintroductionimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tbltag',
            options={'managed': True},
        ),
    ]
