# Generated by Django 4.2.4 on 2023-12-14 08:16

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="company/logs/"),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="company/logs/"),
                ),
                ("content", tinymce.models.HTMLField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
