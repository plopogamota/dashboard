# Generated by Django 4.1.7 on 2023-04-21 09:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_userprofile_follows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="profile_pics"
            ),
        ),
    ]