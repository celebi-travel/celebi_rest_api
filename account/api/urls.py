from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (RegisterView, VerifyEmail, LoginApiView, PasswordTokenCheckAPI,RequestPasswordResetEmail,SetNewPasswordAPIView)

app_name = 'account'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-password/', RequestPasswordResetEmail.as_view(), name='request_reset_password'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name = 'password_reset_confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name = 'password_reset_complete'),

]

"""
Kullanıcılara iki tür token verilir. 1. refresh token 2. access token. 
Access token: kısa süreli kullanımdır. 
Refresh token: Accesse nispeten daha uzun  süre kullanılır. Access token süre dolduğunda refresh token kullanarak
                yeni bir access token oluşturabiliyoruz.
{
  "data": {
    "email": "user@example.com",
    "username": "string",
    "tokens": "{'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9', 
    'access': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'}"
  }
}
"""
