from rest_framework.routers import DefaultRouter
from.views import *
from django.urls import *

route = DefaultRouter()
route.register("login",LoginSet)
route.register("signup",SignupSet)
urlpatterns = [
    path("",include(route.urls)),
    path("email/<str:mail>/",Get_Data_via_Email.as_view())
]