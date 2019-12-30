import json

import demjson
import piexif
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ArtPress import settings
from .models import Medias
from .exif_reader import MediaLibraryExif


class MediaLibrary:
    def __init__(self, request, **kwargs):
        """
        MediaLibrary Control Class

        :param request:
        :param kwargs:
        """
        self.request = request
        self.kwargs = kwargs

    def get_my_medias(self):
        medias = Medias.objects.filter(user_id=1)
        author = self.request.user

        return_datas = []
        for media in medias:
            inf = {
                "id": media.id,
                "author": {
                    "uid": author.id,
                    "name": str(author)
                },
                "filename": media.file,
                "exif": media.exif,
                "rating": media.rating,
                "color": media.color_tag,
                "res": settings.MEDIA_RESOURCES_URL + media.file,
                "thum": settings.MEDIA_RESOURCES_URL + media.file,
                "update_time": media.update_date.strftime('%Y-%m-%d %H:%M:%S'),
                "upload_time": media.upload_date.strftime('%Y-%m-%d %H:%M:%S'),
            }

            return_datas.append(inf)

        return {
            "user": str(self.request.user),
            "data": return_datas,
        }

    def get_medias(self):
        return


""" Request Views """


def ml_getmy_medias(request):
    """
    Get My Medias

    Document:
    /documents/apis.md # /api/medialib/getmymedias/
    """

    # refuse AnonymousUser
    if str(request.user) == "AnonymousUser":
        print(request.user)
        return HttpResponse(json.dumps({"code": 401}), content_type="application/json")

    dat = MediaLibrary(request).get_my_medias()

    dat["code"] = 200

    return HttpResponse(json.dumps(dat), content_type="application/json")


def ml_get_medias(request):
    """
    Get Others Medias

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
