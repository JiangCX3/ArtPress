<<<<<<< HEAD
from django.contrib.auth import logout
=======
from django.contrib.auth import logout, models, authenticate, login
>>>>>>> fa04cec67d2183800edc1645478a2b2a4e2521de
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def ap_manager(request):
    return HttpResponseRedirect("/ap-manager/home/")


def home(request):
<<<<<<< HEAD

=======
>>>>>>> fa04cec67d2183800edc1645478a2b2a4e2521de
    return render(request, 'Manager/home.html', {
        "user": request.user,
    })

<<<<<<< HEAD
def out(request):
    logout(request)
    return HttpResponseRedirect("/user/login/")

def login(request):
=======

def out(request):
    logout(request)
    return HttpResponseRedirect("/ap-manager/user/login/")


def login_p(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username.strip() and password:  # 确保用户名和密码都不为空
            user = authenticate(username=username, password=password)
            if user:
                # 认证成功
                login(request, user)
                return HttpResponseRedirect("/ap-manager/home/")
            else:
                return HttpResponseRedirect("/ap-manager/user/login/?lgstatus=fail")

>>>>>>> fa04cec67d2183800edc1645478a2b2a4e2521de

    return render(request, 'Manager/login.html', {
        "user": request.user,
    })


<<<<<<< HEAD
def register(request):

    return render(request, 'Manager/register.html', {
        "user": request.user,
    })


=======
def register_p(request):
    return render(request, 'Manager/register.html', {
        "user": request.user,
    })
>>>>>>> fa04cec67d2183800edc1645478a2b2a4e2521de
