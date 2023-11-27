from django.db import models

# Create your models here.
class facture(models.Model):
    typefact =models.CharField(max_length=100)
    fraiscoms = models.IntegerField()

class DB(models.Model):
    ncarte = models.IntegerField()
    codesecurite = models.CharField(max_length=100)
    dexpiration = models.DateField()
    email= models.EmailField(max_length=254 )