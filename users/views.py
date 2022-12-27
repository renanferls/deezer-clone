from django.contrib.auth import authenticate
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .renderes import UserRenderer
from .serializers import (
    UserLoginSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
)


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationView(APIView):

    renderer_classes = [UserRenderer]

    @extend_schema(
        request=UserRegistrationSerializer, responses=UserRegistrationSerializer
    )
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response(
            {"user": serializer.data, "token": token},
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):

    renderer_classes = [UserRenderer]

    @extend_schema(request=UserLoginSerializer, responses=UserLoginSerializer)
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        # Auth user
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "message": "Login Success"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"errors": {"non_field_errors": ["Email or Password is not Valid"]}},
                status=status.HTTP_404_NOT_FOUND,
            )


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=UserProfileSerializer, responses=UserProfileSerializer)
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        # responses = None
    )
    def post(self, request):

        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            # unpacking
            user, token = response

        try:
            token = RefreshToken.for_user(user)
            token.blacklist()
            return Response({"message": "Successful logout"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
