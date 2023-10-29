from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import SignUpserializer, UserSerializer


# Create your views here.

@api_view(["POST"])
def register(request):
    data = request.data

    user = SignUpserializer(data=data)
    if user.is_valid():
        if not User.objects.filter(username=data["email"]).exists():
            user = User.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                username=data["email"],
                password=make_password(data["password"]),
            )
            return Response({"details": "User Registered"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "user already exists"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):

    user = UserSerializer(request.user, many=False)

    return Response(user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):

    user = request.user
    data = request.data

    if data.get("first_name"):
        user.first_name = data["first_name"]
    if data.get("last_name"):
        user.last_name = data["last_name"]
    if data.get("username"):
        user.username = data["email"]
    if data.get("email"):
        user.email = data["email"]
    if data.get("password"):
        user.password = make_password(data["password"])

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)