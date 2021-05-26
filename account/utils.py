from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['subject'], body=data['email_body'], to=[data['to']])
        email.send()


# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
#
#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#             print(user.__dict__)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if  user.check_password(password):
#                 return user
#         return None
