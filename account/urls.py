from django.urls import path

from .views import userRegister, userLogin, userLogout

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", userRegister.as_view(), name="user-register"),
    path("login/", userLogin.as_view(), name="user-login"),
    path("logout/", userLogout.as_view(), name="user-logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
