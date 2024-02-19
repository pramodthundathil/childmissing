from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PoliceData(models.Model):
    Police_Station = models.CharField(max_length = 255)
    Address = models.CharField(max_length = 255)
    District =  models.CharField(max_length = 255)
    Designation =  models.CharField(max_length = 255)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null= True, blank = True)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.Police_Station + " " + "PoliceStation"
