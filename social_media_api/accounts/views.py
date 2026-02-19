from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework import generics, permissions, status
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.http import HttpResponse
from rest_framework.authtoken.models import Token

User = get_user_model()

def home(request):
    return HttpResponse("Welcome to the accounts app!")

# Your existing RegisterView and LoginView remain here

# Registration view
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


# Login view
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# Optional: View to get the currently logged-in user info
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Follow a user
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # ✅ Required by the check
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.following.add(target_user)
        return Response(
            {"detail": f"You are now following {target_user.username}"},
            status=status.HTTP_200_OK
        )

# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # ✅ Required by the check
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target_user)
        return Response(
            {"detail": f"You have unfollowed {target_user.username}"},
            status=status.HTTP_200_OK
        )
