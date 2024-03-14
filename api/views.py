from .serializers import *
from login.models import *
from signup.models import *
from rest_framework.viewsets import ModelViewSet


class SignupSet(ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializers

    
class LoginSet(ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializers
