# Generated by Django 2.1.5 on 2019-08-27 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freshman', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freshman',
            old_name='interview_name',
            new_name='interview_id',
        ),
    ]
