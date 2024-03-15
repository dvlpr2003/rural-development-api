from .serializers import *
from login.models import *
from signup.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class SignupSet(ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializers

    
class LoginSet(ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializers

class Get_Data_via_Email(APIView):
    def get_object(self, mail):
        try:
            return Signup.objects.get(mail=mail)
        except Signup.DoesNotExist:
            raise Http404
    def get(self,request,mail):
        snippet = self.get_object(mail = mail)
        serializer = SignupSerializers(snippet)
        return Response(serializer.data)
    