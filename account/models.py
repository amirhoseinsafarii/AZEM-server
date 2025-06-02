from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    role_choises = {"f": "founder", "m": "member"}
    phonNumber = models.IntegerField(blank=True, null=True)
    role = models.CharField(default="m", choices=role_choises, max_length=1)

    def __str__(self):
        return self.username
