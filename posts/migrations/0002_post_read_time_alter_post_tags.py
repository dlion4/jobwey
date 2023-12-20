# Generated by Django 4.2.4 on 2023-12-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="read_time",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="posts.tag"),
        ),
    ]