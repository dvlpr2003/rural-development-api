from django.core.mail import send_mail
from rest_framework import serializers
from login.models import LoginInfo
from signup.models import *
from django.conf import settings


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = "__all__"

class SignupSerializers(serializers.ModelSerializer):
    name = NameSerializers()
    class Meta:
        model  = Signup
        fields = "__all__"
    def create(self, validated_data):
        name_data = validated_data.pop('name')
        mail = validated_data.pop("mail")
        name_instance = Name.objects.create(**name_data)
        signup_instance = Signup.objects.create(name=name_instance, **validated_data)
        # Send confirmation email
        subject = "comming from django server"
        message = "hi da bot uh"
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message,
            from_email,
            [mail],
            fail_silently=False,

        )
        return signup_instance
