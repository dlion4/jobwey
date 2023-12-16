from django.db import models
from companies.models import Job
from account.models import Profile
from django.urls import reverse


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_applicant")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_applicant")
    full_name = models.CharField(max_length=255, help_text="Full Name")
    email_address = models.EmailField(max_length=255)
    phone_number = models.IntegerField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    skills = models.CharField(max_length=1000, help_text="separate multiple skills with a comma", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "-id"


    def split_skills(self):
        if self.skills is not None:
            skills = self.skills.split(",")
            if len(skills)>1:
                return skills[:4]
            return skills
        return None
    
    def __str__(self):
        return self.profile.user.email
    
    def get_resume_filename(self):
        return self.resume.name
    
    def get_absolute_url(self):
        return reverse("applicant:applicant_public_profile", kwargs={"applicant_public_profile_pk": self.profile.pk})
    
    


