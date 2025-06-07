from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from workdesk.models import WorkDesk
from .permissions import AddProjectPermissions, AddMemberToProjectPermissions
from rest_framework.permissions import IsAuthenticated
from .models import Project
from rest_framework import viewsets

# Create your views here.


class ProjectCreate(APIView):

    permission_classes = (AddProjectPermissions,)
    serializer_class = ProjectSerializer  # swagger

    def post(self, request, pk):
        print(request.user.id)

        workdesk = WorkDesk.objects.get(pk=pk)
        # data = request.data.copy()
        # data["creator"] = request.user
        # data["workdesk"] = workdesk
        # data["collaborators"] = request.user

        ser_data = ProjectSerializer(data=request.data, partial=True)

        if ser_data.is_valid():
            project = Project(
                **ser_data.validated_data, creator=request.user, workdesk=workdesk
            )
            print(project)
            project.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AddProjectMember(APIView):

    permission_classes = (AddMemberToProjectPermissions,)
    serializer_class = ProjectSerializer

    def put(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
