from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phoneNumber = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    teamName = models.CharField(max_length=20)

    def __str__(self):
        return self.username
