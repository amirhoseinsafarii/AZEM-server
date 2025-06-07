from rest_framework.permissions import IsAuthenticated
from workdesk.models import WorkDesk, WorkDeskMembership
from .models import Project
from rest_framework import status

from rest_framework.response import Response


class AddProjectPermissions(IsAuthenticated):
    """coustom Permissions"""

    def has_permission(self, request, view):
        if request.data:
            workdeskId = view.kwargs.get("pk")

            workdesk = WorkDesk.objects.get(id=workdeskId)
            print(workdesk, "workdesk name>>>>>>>>>>>>")

            try:
                workdeskfounder = WorkDeskMembership.objects.get(
                    member=request.user, workdeskName=workdesk
                )
                print(workdeskfounder.role, "request user role>>>>>>>>>")
                if workdeskfounder.role != "founder":
                    return False
                else:
                    return True
            except WorkDeskMembership.DoesNotExist:
                return False


class AddMemberToProjectPermissions(IsAuthenticated):
    """coustom Permissions"""

    def has_permission(self, request, view):
        if request.data:
            pId = view.kwargs.get("pk")

            project = Project.objects.get(id=pId)
            print(project, "workdesk name>>>>>>>>>>>>")

            if project.creator == request.user:
                return True
            else:
                return False
