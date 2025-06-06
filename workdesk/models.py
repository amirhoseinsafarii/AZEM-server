from django.db import models

# Create your models here.
from account.models import CustomUser


class WorkDesk(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="workdeskCraetor"
    )
    collaborators = models.ManyToManyField(
        CustomUser, through="WorkDeskMembership", related_name="workdeskCollaborator"
    )


class WorkDeskMembership(models.Model):
    ROLES = (
        ("founder", "founder"),
        ("colaborator", "colaborator"),
    )
    workdeskName = models.ForeignKey(
        WorkDesk, on_delete=models.CASCADE, related_name="members"
    )
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=15, default="colaborator")
