from django import forms

from .models import PostComment, Post



class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['full_name', 'email', 'comment']
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "cols": 4,"rows":4, "placeholder":"comment"}),
        }