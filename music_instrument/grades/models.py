from django.db import models

# Create your models here.
class Grades(models.Model):
    name = models.CharField(max_length=255)
    

class Subgrades(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grades,on_delete=models.CASCADE)
    