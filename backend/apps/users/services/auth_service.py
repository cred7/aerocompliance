from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AuthService:

    @staticmethod
    def login_user(username: str, password: str):
        user = authenticate(username=username, password=password)
        if not user:
            return None

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user,
        }
