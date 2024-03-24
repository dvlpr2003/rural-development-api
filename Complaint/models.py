from django.db import models
from signup.models import Signup

class Complaints (models.Model):
    user = models.ForeignKey(Signup,on_delete = models.CASCADE,null = True)
    ComplaintCategory = models.CharField(max_length = 100,null = True)
    ComplaintName = models.CharField(max_length = 100, null = True)
    ComplaintLocation = models.CharField(max_length = 100,null = True)
    ComplaintDistrict = models.CharField(max_length = 100,null = True)
    ComplaintPincode = models.IntegerField(null = True)
    ComplaintDes = models.TextField(null = True)