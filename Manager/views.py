from django.contrib.auth import logout, models, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def ap_manager(request):
    return HttpResponseRedirect("/ap-manager/home/")


def home(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")

    return render(request, 'Manager/home.html', {
        "user": request.user,
    })


def out(request):
    logout(request)
    return HttpResponseRedirect("/ap-manager/user/login/")


def login_jump(request):
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

    return render(request, 'Manager/login.html', {
        "user": request.user,
    })


def register_p(request):
    return render(request, 'Manager/register.html', {
        "user": request.user,
    })
