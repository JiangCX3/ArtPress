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

    path('ap-manager/', Manager.views.ap_manager),
    path('ap-manager/home/', Manager.views.home),
    path('ap-manager/user/out/', Manager.views.out),
    path('ap-manager/user/login/', Manager.views.login),
    path('ap-manager/user/register/', Manager.views.register),
]
