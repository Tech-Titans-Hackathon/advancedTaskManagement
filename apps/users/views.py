from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,'users/login/login.html')

def signup(request):
    return render(request,'users/signup/signup.html')