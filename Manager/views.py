from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def ap_manager(request):
    return HttpResponseRedirect("/ap-manager/home/")


def home(request):
    print(request.user)
    return render(request, 'Manager/home.html', {
        "user": request.user,
    })
