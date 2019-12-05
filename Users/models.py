from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    nickname = models.CharField('Nick Name', max_length=30, blank=True)
    avatar_filename = models.CharField('Avatar filename', max_length=128, blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)
    bio = models.CharField('Bio', max_length=1024, blank=True)
    url = models.CharField('URL', max_length=128, blank=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()
