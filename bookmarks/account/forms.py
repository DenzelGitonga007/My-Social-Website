from django import forms
# For the registration form
from django.contrib.auth.models import User

# To customize the user profile
from . models import Profile

# Login form
class LoginForm(forms.Form):
    # The input fields
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # the HTML password input type

# User registration class
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    # The class meta ought to be inside the parent class, UserRegistrationForm()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

# Validate password2
def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']

# To customize the user profile
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']