from django import forms
from applicants.models import Application
from companies.models import JobType

class ApplicationForm(forms.ModelForm):
    agree_to_terms = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-check-input", "id": "flexCheckDefault"}))
    class Meta:
        model = Application
        fields = [
            "full_name",
            "email_address",
            "phone_number",
            "resume",
            "skills",
            "agree_to_terms",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email_address": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control"}),
            "resume": forms.FileInput(attrs={"class": "form-control"}),
            "skills": forms.Textarea(attrs={"class": "form-control",}),
        }
