from django import forms
from tinymce import widgets
from .models import Company, Job, JobType 
from ckeditor.widgets import CKEditorWidget
# widget = CKEditorWidget(config_name='awesome_ckeditor')

class CompanyCreateForm(forms.ModelForm):
    logo = forms.FileField(required=False, label="company logo", widget=forms.FileInput(attrs={"class": "form-control"}))
    image = forms.FileField(required=False, label="company image", widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta:
        model = Company
        fields = ["name","location","vision","logo","image","content"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "company name"}),
            "vision": forms.TextInput(attrs={"class": "form-control", "placeholder": "company vision"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "company location"}),
            "content": CKEditorWidget()
        }

class JobCreateForm(forms.ModelForm):
    positions = forms.CharField(label="Number of vacancies", widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "10"}),)
    min_salary = forms.CharField(label="Minumum salary", widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "30,000"}))
    max_salary = forms.CharField(label="Maximum salary", widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "300,000"}),)

    class Meta:
        model = Job
        fields = ["title","positions","location","min_salary","max_salary","content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "position title"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "location of job"}),
            "content": CKEditorWidget()
        }