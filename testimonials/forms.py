from django import forms
from .models import Testimony
from ckeditor.widgets import CKEditorWidget


class TestimonyAdminForm(forms.ModelForm):
    testimony = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Testimony
        fields = ['testimony']
