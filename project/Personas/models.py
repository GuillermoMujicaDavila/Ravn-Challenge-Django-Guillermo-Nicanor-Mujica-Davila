from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE

# Create your models here.

class Person(models.Model):
    personId = models.AutoField(
        primary_key=True,null=False,unique= True,db_column = 'id'
    )    
    personName = models.CharField(
        max_length=200, null=False, db_column='Nombre' 
    )
    personEye = models.CharField(
        max_length=50, null= False, db_column='C_Ojo'
    )
    personHair = models.CharField(
        max_length=50, null=False, db_column='C_Cabello'
    )
    personSkin = models.CharField(
        max_length=50,null=False,db_column='C_Piel'
    )
    personBirth = models.DateField(
        null=False,db_column='Cumpleaños'
    )
    personType = models.CharField(
        max_length=50, null=False,db_column='Tipo'        
    )
    
class Vehicles(models.Model):
    vehiclesId = models.AutoField(
        primary_key=True,null=False,db_column='id'
    )
    vehiclesName = models.CharField(
        max_length=100,null=True,db_column='Nombre'
    )
    personID = models.ForeignKey(Person,on_delete=CASCADE
    )