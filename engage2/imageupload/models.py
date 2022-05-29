from tokenize import Name
from django.db import models

# Create your models here.


class criminal_database(models.Model):
    CriminalName=models.CharField(max_length=100)
    DOB=models.DateTimeField()
    Crimecommited=models.CharField(max_length=100)
    NoOfArrests=models.IntegerField()