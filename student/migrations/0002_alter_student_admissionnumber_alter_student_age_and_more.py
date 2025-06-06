# Generated by Django 5.2.1 on 2025-05-13 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='AdmissionNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000, message='Value must be ≥ 1000'), django.core.validators.MaxValueValidator(5000, message='Value must be ≤ 5000')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(10, message='Value must be ≥ 10'), django.core.validators.MaxValueValidator(120, message='Value must be ≤ 120')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Weight',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(20, message='Value must be ≥ 20'), django.core.validators.MaxValueValidator(120, message='Value must be ≤ 120')]),
        ),
    ]
