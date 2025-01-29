from django.db import models

# Create your models here.
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
