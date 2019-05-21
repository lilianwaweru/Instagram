from .models import Profile

class getProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['infor']
        