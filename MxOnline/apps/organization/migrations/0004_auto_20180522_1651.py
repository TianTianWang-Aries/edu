# Generated by Django 2.0.4 on 2018-05-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180510_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='work_year',
            new_name='work_years',
        ),
    ]
