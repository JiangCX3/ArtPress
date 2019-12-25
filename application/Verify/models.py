from django.db import models

class VerifyCode(models.Model):
    token = models.CharField('TOKEN', max_length=128, blank=True)
    code = models.CharField('CODE', max_length=16, blank=True)
    ip = models.CharField('IP', max_length=128, blank=True)
    create_time = models.DateTimeField('TOKEN', auto_now=True)
