from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [
            'first_name', 'last_name', 'email', 'password','phone_number','date_of_birth',
            'gender','city','address'
        ]

class UserProfile(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = [
            'first_name', 'last_name', 'email', 'password', 'phone_number', 'date_of_birth',
            'gender', 'city', 'address'
        ]
