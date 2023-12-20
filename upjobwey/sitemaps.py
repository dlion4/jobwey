# sitemaps.py
from companies.models import Job
from posts.models import Post


jobs_dict = {
    "queryset": Job.objects.all().order_by("-id"),
    "date_field": "createdAt",
}
posts_dict = {
    "queryset": Post.objects.all().order_by("-id"),
    "date_field": "createdAt",
}