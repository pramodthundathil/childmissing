from django.db import models
from django.contrib.auth.models import User
from Home.models import PoliceData

class MissingChilds(models.Model):
    Child_Name = models.CharField(max_length = 255)
    Age_of_Child = models.IntegerField()
    Address = models.CharField(max_length = 255)
    District =  models.CharField(max_length = 255)
    Missing_From = models.CharField(max_length = 255)
    Phone_number = models.IntegerField()
    Identification_Mark = models.CharField(max_length = 255)
    Description = models.CharField(max_length = 255)
    Photo_Of_Child = models.FileField(upload_to="Missing_Childs")
    Missing_Date = models.DateField(auto_now_add = False)
    status = models.BooleanField(default = True)
    approval_status = models.BooleanField(default = False)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null= True, blank = True)


class FoundChilds(models.Model):
    Child_Name = models.CharField(max_length = 255)
    Age_of_Child = models.IntegerField()
    Address = models.CharField(max_length = 255)
    District =  models.CharField(max_length = 255)
    Find_From = models.CharField(max_length = 255)
    Phone_number = models.IntegerField()
    Identification_Mark = models.CharField(max_length = 255)
    Description = models.CharField(max_length = 255)
    Photo_Of_Child = models.FileField(upload_to="Found_Childs")
    Found_Date = models.DateField(auto_now_add = False)
    status = models.BooleanField(default = True)
    approval_status = models.BooleanField(default = False)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null= True, blank = True)


class PoliceCase(models.Model):
    PoliceStation = models.ForeignKey(PoliceData,on_delete = models.CASCADE)
    Address = models.CharField(max_length = 255)
    District =  models.CharField(max_length = 255)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null= True, blank = True)
    status = models.BooleanField(default = False)
    FIR_Status = models.CharField(max_length = 255,null=True)
    date = models.DateField(auto_now_add = True)
    Insident_Date = models.DateField(auto_now_add = False)
    Compliant = models.CharField(max_length = 2000)
    closingdate = models.DateField(auto_now_add = False,null = True)
    approval_status = models.BooleanField(default = False)


