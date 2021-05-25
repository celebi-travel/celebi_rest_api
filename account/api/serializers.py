from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from account import models


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = models.UserBase
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        print('attrs : ', attrs)
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric character'
            )
        return attrs

        def create(self, validated_data):
            return models.UserBase.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = models.UserBase
        fields = ['token']

class CountrySerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.UserBase
        fields = ('name', 'email', 'country')
