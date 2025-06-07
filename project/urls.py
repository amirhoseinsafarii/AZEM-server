from django.urls import path
from .views import ProjectCreate, AddProjectMember

urlpatterns = [
    path("create-project/<int:pk>/", ProjectCreate.as_view(), name="create-project"),
    path(
        "add-member-project/<int:pk>/",
        AddProjectMember.as_view(),
        name="add-member-project",
    ),
]
