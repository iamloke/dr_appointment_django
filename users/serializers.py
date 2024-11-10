from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'username', 'password', 'is_admin', 'is_manager', 'is_doctor', 'is_patient']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']

        extra_fields = {key: value for key, value in validated_data.items() if key not in ['email', 'username', 'password']}

        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields  
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Authenticate user
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        data['user'] = user
        return data
    
class UserRoleSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['role']

    def get_role(self, obj):
        if obj.is_admin:
            return 'admin'
        elif obj.is_manager:
            return 'manager'
        elif obj.is_doctor:
            return 'doctor'
        elif obj.is_patient:
            return 'patient'
        return 'unknown'