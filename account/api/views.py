from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from . import serializers
from .serializers import EmailVerificationSerializer
from ..models import UserBase
from ..utils import Util
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = UserBase.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('account:email_verify')
        abs_url = 'http://' + current_site + relative_link + '?token=' + str(token)
        email_body = 'Hi ' + user.username + '\n Use link below to verify your email \ndomain:' + abs_url
        data = {'subject': 'Verify Your Email',
                'to': user.email,
                'email_body': email_body}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',
                                           type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')  # get ?token=
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            print(payload)
            user = UserBase.objects.get(id=payload['user_id'])

            if not user.is_active:
                user.is_active = True
                user.save()

            return Response({'email': 'Succesfully activated.'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            # token süresi dolduğunda ...
            return Response({'error': 'This link expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            # token süresi dolduğunda ...
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
