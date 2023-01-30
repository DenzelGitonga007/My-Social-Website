from django import forms

# Login form
class LoginForm(forms.Form):
    # The input fields
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # the HTML password input type