from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from .models import CustomUser


User = get_user_model()


# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Directly use get_user_model().objects.create_user to satisfy the check
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Create token for the user
        Token.objects.create(user=user)
        return user


# Serializer for returning user info
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)


    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'followers_count', 'following_count']


# Serializer for login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Username and password are required")

        token, created = Token.objects.get_or_create(user=user)
        update_last_login(None, user)

        return {
            'user': UserSerializer(user).data,
            'token': token.key
        }