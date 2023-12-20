from tokens.models import TinyMceApiKey
from posts.models import Tag, Post
from django.utils import timezone
import datetime


def get_recent_time():
    return timezone.now() - datetime.timedelta(days=7)


def site_constants(request):
    return dict(

        # socials

        dribbble="jobwey",
        linkedin="jobwey",
        facebook="jobwey",
        instagram="jobwey",
        twitter="jobwey",

        # tinymce key

        tinymce_apikey=TinyMceApiKey.objects.filter(is_active=True).last(),
        tags = Tag.objects.all()[:8],
        recent_posts = Post.objects.filter(createdAt__gte=get_recent_time()).all().order_by("?")[:6],
    )