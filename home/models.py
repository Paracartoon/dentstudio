from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User)
    infodent = models.IntegerField(default=0)
    account = models.TextField(max_length=5500, blank=True)
