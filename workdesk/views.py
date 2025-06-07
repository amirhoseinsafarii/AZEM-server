from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import WorkDesk, WorkDeskMembership
from .serializers import WorkDeskSerializer, WorkDeskMembershipSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class WorkDeskRegister(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = WorkDeskSerializer  # swagger

    def post(self, request):
        print(request.user.id)
        print(request.data["name"])
        ser_data = WorkDeskSerializer(data=request.data)

        if ser_data.is_valid():
            workdesk = WorkDesk(**ser_data.validated_data, creator=request.user)
            workdeskmembership = WorkDeskMembership(
                workdeskName=workdesk, member=request.user, role="founder"
            )
            workdesk.save()
            workdeskmembership.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AddWorkDeskMemberPermissions(IsAuthenticated):
    """coustom Permissions"""

    def has_permission(self, request, view):
        if request.data:
            workdeskId = view.kwargs.get("pk")
            print(workdeskId, "workdeskId ************")
            print(request.user.id, "1")

            workdesk = WorkDesk.objects.get(id=workdeskId)

            print(workdesk.id, "3")
            workdeskfounder = WorkDeskMembership.objects.get(
                member=request.user, workdeskName=workdesk
            )
            print(workdeskfounder.role, "4")
            if workdeskfounder.role != "founder":
                return False
            else:
                return True


class AddWorkDeskMember(APIView):

    permission_classes = (AddWorkDeskMemberPermissions,)
    serializer_class = WorkDeskMembershipSerializer

    def post(self, request, pk):
        workdesk = WorkDesk.objects.get(id=pk)

        data = request.data.copy()
        data["workdeskName"] = workdesk.id
        ser_data = WorkDeskMembershipSerializer(data=data)

        print(ser_data)
        if ser_data.is_valid():
            wm = WorkDeskMembership(**ser_data.validated_data)
            wm.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def workDeskList(request):
    workdesks = WorkDesk.objects.all()
    ser_data = WorkDeskSerializer(workdesks, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def workDeskMembershipList(request):
    workdesks = WorkDeskMembership.objects.all()
    ser_data = WorkDeskMembershipSerializer(workdesks, many=True)
    return Response(ser_data.data)
