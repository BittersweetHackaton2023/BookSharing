from django.contrib.auth.models import AbstractUser
from django.db import models



class Member(models.Model):
    email = models.EmailField(unique=True)
    mileage = models.PositiveIntegerField(default=100)


class Order(models.Model):
    isbn = models.CharField()
    email = models.EmailField(unique=True)
    mileage = models.PositiveIntegerField(default=0)