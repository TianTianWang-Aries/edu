# Generated by Django 2.0.4 on 2018-05-22 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20180522_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='work_year',
            new_name='work_years',
        ),
    ]
