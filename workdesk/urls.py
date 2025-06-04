from django.urls import path

from .views import (
    workDeskList,
    workDeskMembershipList,
    WorkDeskRegister,
    AddWorkDeskMember,
)


urlpatterns = [
    path("lsit-workdesk/", workDeskList, name="workdesk-list"),
    path(
        "lsit-workdeskmembership/",
        workDeskMembershipList,
        name="workdeskmembership-list",
    ),
    path("register-workdesk/", WorkDeskRegister.as_view(), name="workdesk-register"),
    path(
        "add-member-workdesk/<int:pk>/",
        AddWorkDeskMember.as_view(),
        name="workdesk-add-member",
    ),
]
