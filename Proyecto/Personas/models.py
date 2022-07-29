from django.db import models
from datetime import datetime  

class Perfil(models.Model):
    name = models.CharField(max_length=150)
    wager = models.FloatField()
    creation_date = models.DateField(auto_now_add=True,null=True,blank=True)
