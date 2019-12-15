import datetime
import json
import random
import string

from django.http import HttpResponse

import settings
from Verify.models import VerifyCode

from django.shortcuts import render


def create_verify_code(request):
    """
    Create Verify Code


    Return Code:

    CODE    EXPLAIN
    0       OK.
    10      IN COOLDOWN TIME

    """
    # For Nginx Reverse proxy server
    # print(request.META)
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    print(ip)

    # Check IP Cooldown Time
    history_verify_list = VerifyCode.objects.filter(ip=ip)
    if len(history_verify_list) == 0:  # none of history
        return

    for history_verify in history_verify_list:
        code_lifetime = (datetime.datetime.now() - history_verify.create_time).seconds

        if code_lifetime <= settings.VERIFY_CODE_COOLDOWN:
            # In cooldown time
            return HttpResponse(json.dumps({
                "code": "1",
                "message": "IN COOLDOWN TIME!",
            }))
        else:
            # Not in cooldown time
            if code_lifetime > settings.VERIFY_CODE_LIFETIME:  # Delete when lifetime out.
                history_verify.delete()

    token = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    code = ''.join(random.sample(string.ascii_letters + string.digits, settings.VERIFY_CODE_LENGTH))

    VerifyCode.objects.create(
        token=token,
        code=code,
        ip=ip
    )

    return HttpResponse(json.dumps({
        "code": "0",
        "message": token,
    }))
