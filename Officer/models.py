from django.db import models



class Officer(models.Model):
    Officer_mail = models.CharField(max_length = 100,null = False)
    Officer_password = models.CharField(max_length = 100,null = False)
  
    