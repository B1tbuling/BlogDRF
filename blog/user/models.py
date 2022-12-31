from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_status = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'user'
