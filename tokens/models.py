from django.db import models

# Create your models here.

class TinyMceApiKey(models.Model):
    key = models.CharField(max_length=1000, unique=True)
    is_active=models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = '-createdAt'

    def __str__(self):
        return f"{self.pk}"


        