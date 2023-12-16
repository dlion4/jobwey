from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models
from django.db.models import Avg
from tinymce import models as tinymce_models
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    vision = models.CharField(max_length=100, default="Digital Marketing Solutions for Tomorrow")
    logo = models.ImageField(upload_to="company/logs/", blank=True, null=True)
    image = models.ImageField(upload_to="company/logs/", blank=True, null=True)
    content = tinymce_models.HTMLField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    # property

    @property
    def jobs_count(self):
        return self.get_jobs().count()
    @property
    def positions_avg(self):
        try:
            return int(self.get_total_positions()['positions__avg'])
        except:
            return 0
    
    def get_absolute_url(self):
        return reverse("company:company_detail_view", kwargs={"slug": self.slug})
    
    def get_jobs(self):
        return self.company_job.filter(positions__gte=1).all()
    
    def get_total_positions(self):
        try:
            return self.company_job.all().aggregate(Avg("positions"))
        except:
            return 0
    
    
    
class JobType(models.TextChoices):
    FT = "FT", "Full Time"
    PT = "PT", "Part Time"
    RM = "RM", "Remote"


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_job")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    type = models.CharField(max_length=2, choices=JobType.choices, default=JobType.FT)
    positions = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=100, blank=True, null=True)
    min_salary = models.PositiveIntegerField(default=100)
    max_salary = models.PositiveIntegerField()
    content = tinymce_models.HTMLField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title

    # def validate_unique(self, *args, **kwargs):
    #     super().validate_unique(*args, **kwargs)
    #     if self.__class__.objects.filter(company=self.company, title=self.title).exists():
    #         raise ValidationError(message=f'JobRole with this ({self.company}, {self.title}) already exists.', code="unique_together")
    
    def get_applications(self):
        return self.job_applicant.all()
    
    def get_applied_percent(self):
        return int((self.get_applications().count()/self.positions) * 100)

    def get_absolute_url(self):
        return reverse("company:job_detail_view", kwargs={"company_slug": self.company.slug, "job_slug": self.slug})
    
    def get_application_url(self):
        return reverse("applicant:application", kwargs={"company_slug": self.company.slug, "job_slug": self.slug})
    
    def get_create_url(self):
        return reverse("administrator:position-create", kwargs={"company_slug": self.company.slug})
    