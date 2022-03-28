from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class AddUser(models.Model):
    """
    Class to append new user based on built-in class
    """
    categorie = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    area = models.CharField(max_length=264)

    def __str__(self):
        return self.categorie.user.username