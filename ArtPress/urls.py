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

import application.Front.views
import application.Manager.views
import application.Verify.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application.Front.views.index),
    path('post/', application.Front.views.post),

    path('ap-login/', application.Manager.views.login_jump),
    path('ap-manager/', application.Manager.views.ap_manager),
    path('ap-manager/home/', application.Manager.views.home),
    path('ap-manager/ap-cloud/', application.Manager.views.artpress_cloud),
    path('ap-manager/media-manager/', application.Manager.views.media_library),
    path('ap-manager/user/out/', application.Manager.views.out),
    path('ap-manager/user/login/', application.Manager.views.login_p),
    path('ap-manager/user/register/', application.Manager.views.register_p),

    path('ap-manager/user/me/', application.Manager.views.user_me),
    path('ap-manager/user/manager/', application.Manager.views.user_manager),
    path('ap-manager/user/group/', application.Manager.views.user_group),

    path('ap-manager/plugs/templates/', application.Manager.views.plugs_templates),
    path('ap-manager/plugs/plugins/', application.Manager.views.plugs_plugins),

    path('ap-manager/set/common/', application.Manager.views.settings_common),
    path('ap-manager/set/site/', application.Manager.views.settings_site),
    path('ap-manager/set/post/', application.Manager.views.settings_post),
    path('ap-manager/set/safety/', application.Manager.views.settings_safty),

    path('verify/code/create/', application.Verify.views.create_verify_code),

    # Media library APIs
    # Documents at
    path('api/medialib/getmymedias/', application.Manager.views.ml_getmy_medias),
    path('api/medialib/getmedias/', application.Manager.views.ml_get_medias),

    # path('test1/', Front.views.test1),

]
