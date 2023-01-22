from django.db import models

# Create your models here.

class Result(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    blood_pressure = models.IntegerField()
    skin_thickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.IntegerField()
    diabetes_predigree_function = models.FloatField()
    age = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Result2(models.Model):
    age = models.IntegerField()
    sex =  models.IntegerField()
    cp = models.IntegerField()
    trestbps =  models.IntegerField()
    chol =  models.IntegerField()
    fbs =  models.IntegerField()
    restecg =  models.IntegerField()
    thalach =  models.IntegerField()
    exang =  models.IntegerField()
    oldpeak =  models.FloatField(null=True, blank=True)
    slope =  models.IntegerField()
    ca =  models.IntegerField()
    thal =  models.IntegerField()
    target = models.IntegerField(null=True, blank=True)


