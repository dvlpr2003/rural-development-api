from django.db import models
from signup.models import Signup


class Officer(models.Model):
    Officer_mail = models.CharField(max_length = 100,null = False)
    Officer_password = models.CharField(max_length = 100,null = False)
    registered_user =  models.ForeignKey(Signup,on_delete = models.CASCADE)
    