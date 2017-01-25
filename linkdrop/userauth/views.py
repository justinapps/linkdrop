from django.shortcuts import render, redirect
# The following are required for user auth.
from django.contrib.auth.models import User
from userauth.forms import AuthenticateForm, UserCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def index(request, auth_form=None, user_form=None):

    if request.user.is_authenticated():
        user = user.request

    else:
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request, 'index.html', {'user':user})


def user_login(request):
    if request.methon == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())

            #edit this to redirect to user home page.
            return redirect('/')


def user_logout(request):
    logout(request)

    #edit this to redirect back to index page.
    return redirect('/')


def register(request):
    user_form = UserCreateForm(data=request.POST)
    if request.methon == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            #edit this to redirect to user home page.
            return redirect('/')

        else:
            return index(request, user_form=user_form)

        return redirect('/')

