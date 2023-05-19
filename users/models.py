from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


