import json

from django.http import HttpResponse
from django.shortcuts import render


def ml_getmy_medias(request):
    dat = {
        "code": 200,
        "user": str(request.user),
        "data": [
            {
                "id": 1290279,
                "author": {
                    "uid": 2853,
                    "name": "username"
                },
                "res": "https://.../picture.jpg",
                "thum": "http://.../picture.jpg?thumbnails=true",
                "update_time": "1970-1-1 00:00:00"
            },
        ]
    }

    return HttpResponse(json.dumps(dat), content_type="application/json")
