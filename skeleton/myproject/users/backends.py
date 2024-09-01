from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, name=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(name=name)
            if user and check_password(password, user.password):
                # If the password is correct, return the user
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
