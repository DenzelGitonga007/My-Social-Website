# Import Http response
from django.http import HttpResponse
# Default import
from django.shortcuts import render
# Import the authentication framework
from django.contrib.auth import authenticate, login
# Import the LoginForm class
from .forms import LoginForm

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
