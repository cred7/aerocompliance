from rest_framework import viewsets
from apps.users.models.user import User
from apps.users.api.serializers.user_serializer import UserSerializer
from apps.users.permissions.role_permissions import IsAdmin
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def login(self, request):
        from apps.users.services.auth_service import AuthService

        username = request.data.get("username")
        password = request.data.get("password")

        auth_data = AuthService.login_user(username, password)

        if not auth_data:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = self.get_serializer(auth_data["user"])
        return Response(
            {
                "user": serializer.data,
                "access": auth_data["access"],
                "refresh": auth_data["refresh"],
            }
        )
