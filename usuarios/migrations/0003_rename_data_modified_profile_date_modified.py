# Generated by Django 5.0.2 on 2024-02-18 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_profile_data_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='data_modified',
            new_name='date_modified',
        ),
    ]