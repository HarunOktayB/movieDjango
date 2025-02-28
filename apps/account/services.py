# filepath: /c:/Users/PC_6176__/Desktop/myweb/apps/account/services.py
from django.contrib.auth.models import User

class UserCreationService:
    @staticmethod
    def create_user(username, password, email, first_name, user_type):
        if user_type == 'admin':
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                is_staff=True,
                is_superuser=True
            )
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                is_staff=False,
                is_superuser=False
            )
        return user