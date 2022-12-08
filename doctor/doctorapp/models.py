from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.DateField(max_length=10)
    age = models.PositiveBigIntegerField
    gender = models.CharField(max_length=50)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name