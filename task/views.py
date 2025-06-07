from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task


class TaskCreate(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer  # swagger

    def post(self, request):
        print(request.user.id)

        ser_data = TaskSerializer(data=request.data, partial=True)

        if ser_data.is_valid():
            task = Task(**ser_data.validated_data, creator=request.user)
            task.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
