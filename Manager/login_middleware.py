from django.shortcuts import HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/ap-manager/user/login/':
            return
        if request.path == '/ap-manager/user/register/':
            return
        if request.user.is_anonymous:
            return HttpResponseRedirect("/ap-manager/user/login/")
