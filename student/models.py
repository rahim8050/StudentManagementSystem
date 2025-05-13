from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Age = models.PositiveSmallIntegerField(
    validators = [
        MinValueValidator(10, message="Value must be ≥ 10"),
        MaxValueValidator(120, message="Value must be ≤ 120"),
    ]
    )
    Gender = models.CharField(max_length=10)
    Weight = models.PositiveIntegerField(
        validators=[
            MinValueValidator(20, message="Value must be ≥ 20"),
            MaxValueValidator(120, message="Value must be ≤ 120"),
        ]
    )
    Semester = models.PositiveSmallIntegerField(default=0)
    StudentID = models.PositiveIntegerField()
    AdmissionNumber = models.PositiveIntegerField( validators = [
        MinValueValidator(1000, message="Value must be ≥ 1000"),
        MaxValueValidator(5000, message="Value must be ≤ 5000"),
    ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
