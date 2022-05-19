from django import forms

from .models import Saved_labs
from .models import Presaved_labs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryForm(forms.ModelForm):
    class Meta:
        model = Presaved_labs
        fields = ()

class FinalForm(forms.ModelForm):
    class Meta:
        model = Saved_labs
        fields = ()


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=32)
    group = forms.CharField(max_length=64)
    password1 = forms.CharField()
    password2 = forms.CharField()


class SignInForm(forms.Form):
    name = forms.CharField(max_length=32)
    group = forms.CharField(max_length=64)
    password = forms.CharField()


