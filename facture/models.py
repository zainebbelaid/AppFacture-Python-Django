from django.db import models

# Create your models here.
class sc(models.Model):
    username =models.CharField(max_length=100)
    email =models.EmailField(max_length=254 ) 
    message = models.CharField(max_length=100)
  