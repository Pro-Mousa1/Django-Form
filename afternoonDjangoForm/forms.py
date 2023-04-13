from django import forms

# Create a user registration form


class UserRegForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    id_number = forms.CharField()
    date_of_birth = forms.CharField()
    password = forms.CharField()
