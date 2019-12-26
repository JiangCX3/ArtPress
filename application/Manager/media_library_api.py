import json

from django.http import HttpResponse
from django.shortcuts import render


def ml_getmy_medias(request):
    dat = {
        "code": 200
    }
    return HttpResponse(json.dumps(dat), content_type="application/json")
