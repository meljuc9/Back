from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Person(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    fecha= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)