import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ArtPress import settings
from application.Manager.models import Medias


def ml_getmy_medias(request):
    """
    Document:
    /documents/apis.md # /api/medialib/getmymedias/
    """

    # refuse AnonymousUser
    if str(request.user) == "AnonymousUser":
        print(request.user)
        return HttpResponse(json.dumps({"code": 401}), content_type="application/json")

    medias = Medias.objects.filter(user_id=1)
    author = request.user

    return_datas = []
    for media in medias:
        inf = {
            "id": media.id,
            "author": {
                "uid": author.id,
                "name": str(author)
            },
            "res": settings.MEDIA_RESOURCES_URL + settings.MEDIA_LIBRATY_DIR + media.file,
            "thum": settings.MEDIA_RESOURCES_URL + settings.MEDIA_LIBRATY_DIR + media.file,
            "update_time": media.update_date.strftime('%Y-%m-%d %H:%M:%S'),
            "upload_time": media.upload_date.strftime('%Y-%m-%d %H:%M:%S'),
        }

        print(inf)

        return_datas.append(inf)

    dat = {
        "code": 200,
        "user": str(request.user),
        "data": return_datas,
    }

    return HttpResponse(json.dumps(dat), content_type="application/json")


def ml_get_medias(request):
    """
    Document:
    /documents/apis.md # /api/medialib/getmedias/
    """

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
