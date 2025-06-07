from django.urls import path
from .views import TaskCreate

urlpatterns = [path("create-task/", TaskCreate.as_view(), name="create-task")]
