from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from account.models import CustomUser
from workdesk.models import WorkDesk


class Project(models.Model):
    projectTitle = models.CharField(max_length=50)
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="projectCraetor"
    )
    collaborators = models.ManyToManyField(
        CustomUser, related_name="projectCollaborators"
    )
    workdesk = models.ForeignKey(WorkDesk, on_delete=models.CASCADE)
