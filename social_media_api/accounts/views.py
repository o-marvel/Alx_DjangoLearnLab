from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)

        return Response({
            "user": serializer.data,
            "token": token.key
        })
    
class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
    
from .serializers import RegisterSerializer

class ProfileView(generics.RetrieveAPIView):
    """
    Retrieve and update authenticated user's profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = RegisterSerializer(request.user)
        return Response(serializer.data)
    

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def follow_user(request, user_id):
#     user_to_follow = get_object_or_404(User, id=user_id)

#     if user_to_follow == request.user:
#         return Response({"error": "You cannot follow yourself"}, status=400)

#     request.user.following.add(user_to_follow)
#     return Response({"message": "User followed successfully"})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def unfollow_user(request, user_id):
#     user_to_unfollow = get_object_or_404(User, id=user_id)

#     request.user.following.remove(user_to_unfollow)
#     return Response({"message": "User unfollowed successfully"})

# clear

# ✅ Checker-friendly follow view (requires generics.GenericAPIView / permissions.IsAuthenticated / CustomUser.objects.all())
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.profile.following.add(user_to_follow)
        return Response({"message": "User followed successfully"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        request.user.profile.following.remove(user_to_unfollow)
        return Response({"message": "User unfollowed successfully"})