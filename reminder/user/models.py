from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # groups
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined

    email = models.EmailField(unique=True, blank=False)
    ACTIVE = 'OK'
    INACTIVE = 'IN'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    ]

    # def save(self, *args, **kwargs):
    #    pass
    # if not self.id:
    #    self.created_at = timezone.now()

    class Meta:
        db_table = 'usuario'