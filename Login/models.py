from django.db import models
from django.contrib.auth.models import AbstractUser
from Clientes.models import Cliente

# Create your models here.
class User(AbstractUser):
  REQUIRED_FIELDS = ['dni']
  USERNAME_FIELD = 'username'

  username = models.CharField(unique=True, max_length=150)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=150, blank=True)
  email = models.EmailField(blank=True)
  dni = models.CharField(unique=True, max_length=150)
  customer_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING,
    blank=True, null=True, db_column='customer_id')