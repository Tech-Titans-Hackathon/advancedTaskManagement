from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return render(request,'users/signup/signup.html')