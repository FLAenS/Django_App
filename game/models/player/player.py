from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # when user deleted, delete the associated player
    photo = models.URLField(max_length=256, blank=True)

    def __str__(self):  # the displayed player name
        return str(self.user)
