from rest_framework.routers import DefaultRouter
from.views import *
from django.urls import *

route = DefaultRouter()
route.register("signup",SignupSet)
route.register("complaints",ComplaintSet)
urlpatterns = [

    path("",include(route.urls)),
    path("email/<str:mail>/password/<str:password>/",Get_Login.as_view()),#login end point
    path("email/<str:mail>/otp/<str:otp>/",Verify_otp.as_view()),#otp verifying page
    path("complaint/<str:mail>/",RaiseComplaint.as_view()), #complaint raising end point
    path("total_user/",UserCount.as_view()),#get total user count
    path("total_complaint/",TotalComplaints.as_view()),#get total complaints
    path("get_user/<int:id>/",GetUSERdetails.as_view()), #get user detail using id
    path("officer_login/<str:mail>/password/<str:password>/",Officer_Login.as_view()), #officer login
    path("Complaint/<str:mail>/Accept/<int:id>/",AcceptComplaint.as_view()) # complaint accepted
]
