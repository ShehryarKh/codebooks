from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField()
    pass