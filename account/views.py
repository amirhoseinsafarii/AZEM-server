from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

# Create your views here.


class userRegister(APIView):
    def post(self, request):

        ser_data = UserSerializer(data=request.data)

        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class userLogin(APIView):
    def post(self, request):
        phoneNumber = request.data.get("phoneNumber")
        password = request.data.get("password")
        user = None
        if phoneNumber and password:
            user = CustomUser.objects.get(phoneNumber=phoneNumber, password=password)
            refresh = RefreshToken.for_user(user)

            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"error": "user not found"}, status=status.HTTP_400_BAD_REQUEST
            )


class userLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"e": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
