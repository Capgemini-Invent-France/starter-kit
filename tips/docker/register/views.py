# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import auth


used_url = "http://127.0.0.1:8000/"


def register(response):
    
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()   
            return redirect(used_url + "login")
    else:
        form = RegisterForm()
        context = {"form":form}
        return render(response,"register/register.html", context)


def log_out(request):
    if request.method == "POST":
        auth.logout(request)
        print("logout")
        return redirect(used_url + "login")