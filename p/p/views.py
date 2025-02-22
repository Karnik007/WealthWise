from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def signup(request):
    return render(request, 'website/signup.html')

def login(request):
    return render(request, 'website/login.html')