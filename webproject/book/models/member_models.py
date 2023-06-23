from django.db import models

class Member:
    email = models.EmailField(unique=True)
    mileage = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.email