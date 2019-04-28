# Generated by Django 2.0.4 on 2018-06-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_video_learn_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='教师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='youneed_know',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]
