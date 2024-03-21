from django.db import models


class Signup(models.Model):
    fname = models.CharField(max_length = 100,null = True)
    lname = models.CharField(max_length =100,null = True)
    mail = models.EmailField(max_length = 100,null = False,unique = True)
    password = models.CharField(max_length = 100,null = True)
    phone = models.IntegerField(unique = True, null = False)
    address = models.CharField(max_length = 100,null = False)
    district = models.CharField(max_length = 100,null = False)
    pincode = models.IntegerField(null = False)
    otp = models.CharField(null = True,max_length = 100)
    
