from django.urls import path
from .views import RegisterView, VerifyEmail,LoginApiView

app_name = 'account'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email_verify'),
]
