# Generated by Django 2.0.4 on 2018-05-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.IntegerField(default=11, verbose_name='手机'),
        ),
    ]