from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponse
def home(request):
    return render(request, 'WW/home.html')

def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return HttpResponse('You are already logged in')
        return redirect('home')
    login_form = LoginForm()
    signup_form = SignupForm()
    if request.method == 'POST':
        if 'login' in request.POST: 
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                try:
                    user = User.objects.get(email=email)
                    if check_password(password, user.password):
                        return redirect('home') 
                    else:
                        login_form.add_error('password', 'Incorrect password.')
                except User.DoesNotExist:
                    login_form.add_error('email', 'User does not exist.')
        elif 'signup' in request.POST: 
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.password = make_password(signup_form.cleaned_data['password'])
                user.save()
                return redirect('home')  

    return render(request, 'WW/signup.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

def i1(request):
    return render(request, 'WW/i1.html/')
