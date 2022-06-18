from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    image = models.ImageField(upload_to = "profile_pics", blank = True )
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user, 'Profile')

    class Meta : 
        verbose_name_plural = "USER PROFILES"