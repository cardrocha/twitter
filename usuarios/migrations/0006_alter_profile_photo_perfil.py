# Generated by Django 5.0.2 on 2024-02-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_profile_photo_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
