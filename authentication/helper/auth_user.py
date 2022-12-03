from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
        return authenticate(username=user.username, password=password)
    except User.DoesNotExist:
        print("user does not exist")
        return None