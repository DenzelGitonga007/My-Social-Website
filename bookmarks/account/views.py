# Import Http response
from django.http import HttpResponse
# Default import
from django.shortcuts import render
# Import the authentication framework
from django.contrib.auth import authenticate, login
# Import the LoginForm class
from .forms import LoginForm, UserRegistrationForm
# Using default auth framework for login view
from django.contrib.auth.decorators import login_required

# The profile model
from . models import Profile

# Create your views here.
# User login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # instantiate the form
        if form.is_valid(): # validate the inputs submitted
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd['username'],
                password = cd['password']
                ) # authenticate the user from the db
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticate successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Default login view
@login_required
def dashboard(request):
    return render(request,
    'dashboard.html',
    {'section': 'dashboard'}
    )

# User registration
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            # Create a user profile object associated with the user account created
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})