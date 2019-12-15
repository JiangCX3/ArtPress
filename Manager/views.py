from django.contrib.auth import logout, models, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Users.models import UserProfile
from ArtPress import settings

""" Manly """


def ap_manager(request):
    return HttpResponseRedirect("/ap-manager/home/")


def home(request):
    return render(request, 'Manager/home.html', {
        "user": request.user,
    })


def artpress_cloud(request):
    return render(request, 'Manager/artpress-cloud.html', {
        "user": request.user,
    })


""" Accounts """


def user_group(request):
    return render(request, 'Manager/user/group.html', {
        "user": request.user,
    })


def user_manager(request):
    return render(request, 'Manager/user/manager.html', {
        "user": request.user,
    })


def user_me(request):
    # == Get User Profiles ==

    # Assembly avatar file path
    up = UserProfile.objects.get(user=request.user)
    avatar_path = settings.USER_AVATAR_STATIC_PATH + up.avatar_filename

    """Post"""
    if request.method == "POST":
        # new一个userprofile 字段
        userprofile = UserProfile.objects.get(user_id=request.user.id)
        user = request.user

        # 这是根据标签来分类的
        content_type = request.POST.get('type')
        if content_type == "base":
            """ Base Profile """
            f_name = request.POST.get('first-name')
            l_name = request.POST.get('last-name')
            bio = request.POST.get('bio')
            url = request.POST.get('url')

            # 检查长度
            if len(bio) >= 512:
                raise RuntimeError('Bio length is over 512!')

            if len(url) >= 128:
                raise RuntimeError('URL length is over 512!')

            # 写入user.profile

            userprofile.bio = bio
            userprofile.url = url
            user.first_name = f_name
            user.last_name = l_name

        userprofile.save()
        user.save()

        HttpResponseRedirect("/ap-manager/user/me/")

    return render(request, 'Manager/user/me.html', {
        "user": request.user,
        "avatar_path": avatar_path,
        "setting_email_cooldown": settings.VERIFY_CODE_EMAIL_COOLDOWN,
    })


""" Plugs """


def plugs_plugins(request):
    return render(request, 'Manager/plugs/plugins.html', {
        "user": request.user,
    })


def plugs_templates(request):
    return render(request, 'Manager/plugs/templates.html', {
        "user": request.user,
    })


""" Settings """


def settings_common(request):
    return render(request, 'Manager/settings/common.html', {
        "user": request.user,
    })


def settings_post(request):
    return render(request, 'Manager/settings/post.html', {
        "user": request.user,
    })


def settings_safty(request):
    return render(request, 'Manager/settings/safty.html', {
        "user": request.user,
    })


def settings_site(request):
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
