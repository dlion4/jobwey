from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from account.models import Profile

class Testimony(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="profile_testimony")
    testimony = RichTextField()
    is_positive = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonies"

    def __str__(self):
        return str(self.pk)
    