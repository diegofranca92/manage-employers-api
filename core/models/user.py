from django.db import models
from django.contrib.auth.models import AbstractUser
# https://dev.to/ki3ani/implementing-jwt-authentication-and-user-profile-with-django-rest-api-part-3-3dh9

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    permission = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)