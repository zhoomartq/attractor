from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from user.serializers import UserListSerializer
from . import serializers
from user.send_mail import send_confirmation_email

User = get_user_model()


class RegisterAPIView(APIView):

    def post(self, request):
        serializer = serializers.RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'Account Activated'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'Your Link expired'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


class PermissionMixin:

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAdminUser, ]
        elif self.action == 'list':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

class UserListView(PermissionMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

