from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'role']


# class AccountCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = Account
#         fields = ['email', 'first_name', 'last_name', 'role', 'password']

#     def create(self, validated_data):
#         return Account.objects.create_user(**validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parollar mos kelmadi"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return Account.objects.create_user(**validated_data, role='Student')
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email va parol kerak")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Email yoki parol xato")
        if user.role != 'Student':
            raise serializers.ValidationError("Foydalanuvchi Student emas")