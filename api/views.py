from .serializers import *
from signup.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from Complaint.models import Complaints


class SignupSet(ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializers
class ComplaintSet(ModelViewSet):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializers
# data fetching via mail
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
    
# otp verification end point
class Verify_otp(APIView):
    def get_object(self,mail):
        try:
            return Signup.objects.get(mail=mail)
        except Signup.DoesNotExist:
            raise Http404
    def get(self,request,mail,otp):
        snippet = self.get_object(mail = mail)
        if snippet.otp == otp:
            return Response({"Success"})
        return Response({"Invalid OTP"})



