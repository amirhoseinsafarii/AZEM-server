from django.contrib import admin

# Register your models here.

from .models import Task


@admin.register(Task)
class TaslAdmin(admin.ModelAdmin):
    list_display = ["taskTitle", "dedline", "taskProject", "taskStatus", "creator"]
