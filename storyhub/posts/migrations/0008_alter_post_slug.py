# Generated by Django 4.1.7 on 2023-09-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_postviews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]