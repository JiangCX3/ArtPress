from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def ap_manager(request):
    return HttpResponseRedirect("/ap-manager/home/")


def home(request):

    return render(request, 'Manager/home.html', {
        "user": request.user,
    })

def out(request):
    logout(request)
    return HttpResponseRedirect("/user/login/")

def login(request):

    return render(request, 'Manager/login.html', {
        "user": request.user,
    })


def register(request):

    return render(request, 'Manager/register.html', {
        "user": request.user,
    })


