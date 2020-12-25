from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
from user_profile.models import LeaveApplication
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        label = "password",
        widget = forms.PasswordInput()
    )
    

class SigninForm(forms.Form):

    username = forms.CharField(max_length=20)
    password = forms.CharField(
        label = "password",
        widget = forms.PasswordInput()
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Wrong username or password")
        return username

class Img(forms.Form):
    img = forms.ImageField()


class LeaveForm(forms.ModelForm):
    

    class Meta:
        model = LeaveApplication
        fields = ('reason',)

        widgets = {
            'reason' : forms.TextInput
        }

      



