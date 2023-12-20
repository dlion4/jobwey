# Generated by Django 4.2.4 on 2023-12-20 12:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100)),
                (
                    "country_flag",
                    models.ImageField(blank=True, upload_to="country_flag/"),
                ),
                ("summary", models.TextField()),
                ("content", tinymce.models.HTMLField()),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Visa",
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
                ("country", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100)),
                ("content", tinymce.models.HTMLField()),
            ],
        ),
    ]