from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.TextField()

class Assignment(models.Model):
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="assignments")

class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    students = models.ManyToManyField(User, related_name="courses")  # Many-to-many relationship with students
    # assignment_set
