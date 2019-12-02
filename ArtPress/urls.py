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

import Front.views
import Manager.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Front.views.index),
    path('post/', Front.views.post),

    path('ap-login/', Manager.views.login_jump),
    path('ap-manager/', Manager.views.ap_manager),
    path('ap-manager/home/', Manager.views.home),
    path('ap-manager/ap-cloud/', Manager.views.artpress_cloud),
    path('ap-manager/user/out/', Manager.views.out),
    path('ap-manager/user/login/', Manager.views.login_p),
    path('ap-manager/user/register/', Manager.views.register_p),

    path('ap-manager/user/me/', Manager.views.user_me),
    path('ap-manager/user/manager/', Manager.views.user_manager),
    path('ap-manager/user/group/', Manager.views.user_group),

    path('ap-manager/plugs/templates/', Manager.views.plugs_templates),
    path('ap-manager/plugs/plugins/', Manager.views.plugs_plugins),

    path('ap-manager/set/common/', Manager.views.settings_common),
    path('ap-manager/set/site/', Manager.views.settings_site),
    path('ap-manager/set/post/', Manager.views.settings_post),
    path('ap-manager/set/safety/', Manager.views.settings_safty),
]
