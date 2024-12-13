from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return(self.user.username, "profile")
	


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    # Указание related_name для устранения конфликта
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Уникальное имя для обратной ссылки
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Уникальное имя для обратной ссылки
        blank=True
    )