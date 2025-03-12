from django.db import models

class DebitCart(models.Model):
    owner = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(max_length=12, unique=True)
    national_id = models.IntegerField(unique=True)
    age = models.PositiveIntegerField()




