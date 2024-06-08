from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

# Create your models here.

class Visa(models.Model):
    country = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    content = RichTextField()

    def get_absolute_url(self):
        return reverse("jobwey:visa_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.country
    


class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    country_flag = models.ImageField(upload_to="country_flag/", blank=True)
    summary = models.TextField()
    content = RichTextField()
    country = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("jobwey:service_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return str(self.title)


