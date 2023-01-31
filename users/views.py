from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    CreateUserSerializer, ViewUsersSerializer
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['fullname'] = user.fullname
        token['jamb_reg_num'] = user.jamb_reg_num
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# jamb_reg = 75742946GB
# password = Ahmed@23

# @permission_classes([IsAuthenticated]) --- for function views
# permission_classes = [IsAuthenticated] --- for class views

class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny,]

    def create(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User Created Successfully",
                "user_data": serializer.data,
                
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
        )


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ViewUsersSerializer


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Request):
        
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            print(refresh_token)

            return Response(data={"message": "Successfully Blacklisted"}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


