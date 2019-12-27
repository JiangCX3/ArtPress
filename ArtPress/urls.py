"""ArtPress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import Application.Front.views
import Application.Manager.views
import Application.Verify.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Application.Front.views.index),
    path('post/', Application.Front.views.post),

    path('ap-login/', Application.Manager.views.login_jump),
    path('ap-manager/', Application.Manager.views.ap_manager),
    path('ap-manager/home/', Application.Manager.views.home),
    path('ap-manager/ap-cloud/', Application.Manager.views.artpress_cloud),
    path('ap-manager/media-manager/', Application.Manager.views.media_library),
    path('ap-manager/user/out/', Application.Manager.views.out),
    path('ap-manager/user/login/', Application.Manager.views.login_p),
    path('ap-manager/user/register/', Application.Manager.views.register_p),

    path('ap-manager/user/me/', Application.Manager.views.user_me),
    path('ap-manager/user/manager/', Application.Manager.views.user_manager),
    path('ap-manager/user/group/', Application.Manager.views.user_group),

    path('ap-manager/plugs/templates/', Application.Manager.views.plugs_templates),
    path('ap-manager/plugs/plugins/', Application.Manager.views.plugs_plugins),

    path('ap-manager/set/common/', Application.Manager.views.settings_common),
    path('ap-manager/set/site/', Application.Manager.views.settings_site),
    path('ap-manager/set/post/', Application.Manager.views.settings_post),
    path('ap-manager/set/safety/', Application.Manager.views.settings_safty),

    path('verify/code/create/', Application.Verify.views.create_verify_code),

    # Media library APIs
    # Documents at
    path('api/medialib/getmymedias/', Application.Manager.views.ml_getmy_medias),

    # path('test1/', Front.views.test1),

]
