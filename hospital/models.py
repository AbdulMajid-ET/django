
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patients'
    )

    def __str__(self):
        return self.name
