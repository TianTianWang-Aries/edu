# Generated by Django 2.0.4 on 2018-06-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_auto_20180618_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, verbose_name='接收用户'),
        ),
    ]
