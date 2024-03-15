from django.db import models

class Name(models.Model):
    fname = models.CharField(max_length = 100,null = False)
    lname = models.CharField(max_length = 100,null = False)
    def __str__(self):
        return f"{self.fname}.{self.lname}"

class Signup(models.Model):
    name = models.OneToOneField(Name,on_delete = models.CASCADE,null = False)
    mail = models.EmailField(max_length = 100,null = False,unique = True)
    password = models.CharField(max_length = 100,null = True)
    phone = models.IntegerField(unique = True, null = False)
    address = models.CharField(max_length = 100,null = False)
    district = models.CharField(max_length = 100,null = False)
    pincode = models.IntegerField(null = False)
