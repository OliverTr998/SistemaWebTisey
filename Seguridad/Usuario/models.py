from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    pass

    class Meta:
        db_table = 'Usuario'