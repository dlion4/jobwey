# Generated by Django 4.2.4 on 2024-06-08 15:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
