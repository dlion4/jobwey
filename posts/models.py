from django.urls import reverse
from django.db import models
from tinymce import models as tinymce_models
from account.models import Profile
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category")
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="posts/")
    content = RichTextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    read_time = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"post_slug": self.slug})
    
    def get_comments(self):
        return self.post_comment.all().order_by("-id")
    
    def get_read_time(self):
        return int(len(str(self.content)) / 100)
    
    def save(self, *args, **kwargs):
        self.read_time = self.get_read_time()
        return super().save(*args, **kwargs)
    


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_name)


