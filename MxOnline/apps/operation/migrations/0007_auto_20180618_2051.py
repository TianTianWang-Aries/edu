# Generated by Django 2.0.4 on 2018-06-18 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_remove_coursecomments_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '用户学习过的课程', 'verbose_name_plural': '用户学习过的课程'},
        ),
    ]