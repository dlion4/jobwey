# Generated by Django 4.2.4 on 2023-12-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_post_read_time_alter_post_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="postcomment",
            name="profile",
        ),
        migrations.AddField(
            model_name="postcomment",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="postcomment",
            name="full_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
