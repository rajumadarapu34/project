from django import forms
from django.contrib.auth.models import User
from .models import Student
from .models import Marks


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['course', 'phone']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'score']
