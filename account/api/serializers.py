from django.contrib.auth import authenticate
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from account import models

from account.models import UserBase


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = UserBase
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        # Todo email ve diğerlerini check et
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric character'
            )
        return attrs

    def create(self, validated_data):
        return UserBase.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = UserBase
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = UserBase
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        # import pdb
        # pdb.set_trace()
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin.')
        if not user.is_verified:
            raise AuthenticationFailed('Email is note verified. ')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
        return super(LoginSerializer, self).validate(attrs)
