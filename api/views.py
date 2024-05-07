from .serializers import *
from signup.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from Complaint.models import Complaints
from Officer.models import Officer


class SignupSet(ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializers


class ComplaintSet(ModelViewSet):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializers
    

class Get_Login(APIView):
    def get_object(self, mail):
        try:
            return Signup.objects.get(mail=mail)
        except Signup.DoesNotExist:
            raise Http404
    
    def get(self,request,mail,password):
        snippet = self.get_object(mail = mail)

        print(snippet)
        if snippet.password == password:

            return Response({"status":"success"})
        return Response({"status":"invalid password"})
        
    
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
    

#complaint raising operations
    


class RaiseComplaint(APIView):
    def get_object(self,mail):
        try:
            return Signup.objects.get(mail=mail)
        except Signup.DoesNotExist:
            raise Http404
    def post(self,request,mail):
        snippet = self.get_object(mail = mail)
        ComplaintCategory=request.data.get("ComplaintCategory")
        ComplaintImage=request.data.get("ComplaintImage")
        ComplaintName=request.data.get("ComplaintName")
        ComplaintLocation=request.data.get("ComplaintLocation")
        ComplaintDistrict=request.data.get("ComplaintDistrict")
        ComplaintPincode=request.data.get("ComplaintPincode")
        ComplaintDes=request.data.get("ComplaintDes")
        Complaints.objects.create(user=snippet,ComplaintCategory=ComplaintCategory,ComplaintImage=ComplaintImage,ComplaintName=ComplaintName,ComplaintLocation=ComplaintLocation,ComplaintDistrict=ComplaintDistrict,ComplaintPincode=ComplaintPincode,ComplaintDes=ComplaintDes)
        return Response({"hi":"success"})
    
#Registered user count
class UserCount(APIView):
    def get(self,request):
        count = Signup.objects.all().count()
        return Response({
            "total":count
        })


#total complaints
class TotalComplaints(APIView):
    def get(self,request):
        count = Complaints.objects.all().count()
        return Response({
            "total":count
        })
    

class GetUSERdetails(APIView):
    def get_object(self,id):
        try:
            return Signup.objects.get(id=id)
        except Signup.DoesNotExist:
            raise Http404
    def get(self,request,id):
        snippet = self.get_object(id = id)
        user = UserDetailSerializer(snippet)
        return Response(user.data)
    



class Officer_Login(APIView):
    def get_object(self, mail):
        try:
            return Officer.objects.get(Officer_mail=mail)
        except Officer.DoesNotExist:
            raise Http404
    
    def get(self,request,mail,password):
        snippet = self.get_object(mail = mail)

        if snippet.Officer_password == password:

            return Response({"status":"success"})
        return Response({"status":"invalid password"})
    

class AcceptComplaint(APIView): #Accept complaint
    def get_object(self,id):
        try:
            return Complaints.objects.get(id=id)
        except Complaints.DoesNotExist:
            raise Http404

    def post(self,request,id,mail):
        AlterData = self.get_object(id)
        AlterData.Accepted = True
        AlterData.save()
            
        send_mail(
            'Complaint accepted',
            f'your complaint was accepted by the officer',
            'gayathrigaya698@gmail.com',  
            [mail],      
            fail_silently=False,)
        return Response({"status":"success"})
    

class forgetpassword(APIView): #forgetpassword
    def get_object(self,mail):
        try:
            return Signup.objects.get(mail = mail)
        except Complaints.DoesNotExist:
            raise Http404
    def post(self,request,mail):
        gmail = self.get_object(mail)
        send_mail(
            'Forget password',
            f'your otp is {gmail.otp}',
            'gayathrigaya698@gmail.com',
            [mail],
            fail_silently=False,)
        return Response({"status":"success"})
    
class Verify_forget_otp(APIView):
    def get_object(self,mail):
        try:
            return Signup.objects.get(mail=mail)
        except Signup.DoesNotExist:
            raise Http404
    def get(self,request,mail,otp):
        snippet = self.get_object(mail = mail)
        if snippet.otp == otp:

            send_mail(

                'Forget password',
                f'your otp is {snippet.password}',
                'gayathrigaya698@gmail.com',

                [mail],
                fail_silently=False,)
            return Response({"Success"})
        return Response({"Invalid OTP"})
        