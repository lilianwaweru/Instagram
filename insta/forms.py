from .models import Profile
from django import forms

class getProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['infor']
