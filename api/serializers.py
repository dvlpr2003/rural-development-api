from rest_framework import serializers
from login.models import LoginInfo
from signup.models import *


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
        name_instance = Name.objects.create(**name_data)
        signup_instance = Signup.objects.create(name=name_instance, **validated_data)
        return signup_instance
