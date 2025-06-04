from django.contrib import admin

from .models import WorkDesk, WorkDeskMembership

# Register your models here.


@admin.register(WorkDesk)
class WorkDeskAdmin(admin.ModelAdmin):
    list_display = ["name", "creator"]


@admin.register(WorkDeskMembership)
class WorkDeskMembership(admin.ModelAdmin):
    list_display = ["workdeskName", "member", "role"]
