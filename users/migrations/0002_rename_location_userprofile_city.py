# Generated by Django 5.0.1 on 2025-05-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='city',
        ),
    ]
