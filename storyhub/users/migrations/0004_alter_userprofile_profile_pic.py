# Generated by Django 4.1.7 on 2023-03-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics"),
        ),
    ]