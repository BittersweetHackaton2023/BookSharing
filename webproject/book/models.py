from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


class Member(models.Model):
    email = models.EmailField(unique=True)
    mileage = models.IntegerField(default=100)


class Order(models.Model):
    isbn = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    mileage = models.PositiveIntegerField(default=0)

