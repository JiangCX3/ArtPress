from django.db import models


# Create your models here.

class Medias(models.Model):
    file = models.CharField('Manager filepath', max_length=128)
    user_id = models.IntegerField('Author ID', null=True)
    exif = models.TextField('Exif Encoded Data', null=True)