from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

