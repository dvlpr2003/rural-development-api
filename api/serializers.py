from django.core.mail import send_mail
from rest_framework import serializers
from signup.models import *
import string
import random




class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Signup
        fields = "__all__"
    def create(self, validated_data):
        otp = ''.join(random.choices(string.digits, k=6))
        signup_instance = Signup.objects.create(**validated_data)
        signup_instance.otp = otp
        signup_instance.save()
        send_mail(
                'Your OTP',
                f'Your OTP is: {otp}',
                "gayathrigaya698@gmail.com",  
                [signup_instance.mail],      
                fail_silently=False,)
       
        return signup_instance

        
