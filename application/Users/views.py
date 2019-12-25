from django.contrib.auth import logout, models, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def change_password(request):
    return