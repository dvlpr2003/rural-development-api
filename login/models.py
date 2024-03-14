from django.db import models

class LoginInfo(models.Model):
    user_name = models.CharField(max_length = 100,null = False,unique = True)
    password = models.CharField(max_length = 100,null = False)


    def __str__(self):
        return f"{self.user_name}"