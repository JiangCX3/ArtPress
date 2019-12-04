from django.contrib.auth import logout, models, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Users.models import UserProfile
from ArtPress import settings

""" Manly """


def ap_manager(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
        # =======

    return HttpResponseRedirect("/ap-manager/home/")


def home(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/home.html', {
        "user": request.user,
    })


def artpress_cloud(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/artpress-cloud.html', {
        "user": request.user,
    })


""" Accounts """


def user_group(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/user/group.html', {
        "user": request.user,
    })


def user_manager(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/user/manager.html', {
        "user": request.user,
    })


def user_me(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======


    # == Get User Profiles ==

    # Assembly avatar file path
    up = UserProfile.objects.get(user=request.user)
    avatar_path = settings.USER_AVATAR_STATIC_PATH + up.avatar_filename

    return render(request, 'Manager/user/me.html', {
        "user": request.user,
        "avatar_path": avatar_path,
    })


""" Plugs """


def plugs_plugins(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/plugs/plugins.html', {
        "user": request.user,
    })


def plugs_templates(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/plugs/templates.html', {
        "user": request.user,
    })


""" Settings """


def settings_common(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/settings/common.html', {
        "user": request.user,
    })


def settings_post(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/settings/post.html', {
        "user": request.user,
    })


def settings_safty(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/settings/safty.html', {
        "user": request.user,
    })


def settings_site(request):
    # 认证，匿名用户则跳转给登录页面
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect("/ap-manager/user/login/")
    # =======

    return render(request, 'Manager/settings/site.html', {
        "user": request.user,
    })


""" The User activity views"""


def out(request):
    logout(request)
    return HttpResponseRedirect("/ap-manager/user/login/")


def login_jump(request):
    return HttpResponseRedirect("/ap-manager/user/login/")


""" Login, register and Logout views """


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
