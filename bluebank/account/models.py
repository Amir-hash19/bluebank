from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Profile(models.Model):
    name = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(unique=True)
    gmail = models.EmailField(null=True, blank=True)
    address = models.TextField()


