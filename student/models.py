from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Age = models.PositiveSmallIntegerField(default=0)
    Gender = models.CharField(max_length=10)
    Weight = models.PositiveIntegerField(default=0)
    Semester = models.PositiveSmallIntegerField(default=0)
    StudentID = models.PositiveIntegerField()
    AdmissionNumber = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
