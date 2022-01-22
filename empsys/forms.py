from django import forms
from .models import Employee


class EmployeeAdder(forms.Form):
    ename = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    address = forms.CharField(widget=forms.TextInput())
    salary = forms.IntegerField()

    class Meta:
        model = Employee
        fields = ['ename', 'email', 'address', 'salary']


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
