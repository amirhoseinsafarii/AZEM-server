from django.db import models
from account.models import CustomUser
from project.models import Project

# Create your models here.


class Task(models.Model):
    STATUS = (
        ("to do", "to-do"),
        ("doing", "doing"),
        ("done", "done"),
    )
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=500, null=True, blank=True)
    dedline = models.DateTimeField()
    doers = models.ManyToManyField(CustomUser, related_name="taskdoers")
    taskProject = models.ForeignKey(Project, on_delete=models.CASCADE)
    taskStatus = models.CharField(choices=STATUS, default="to do", max_length=20)
    creator = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
