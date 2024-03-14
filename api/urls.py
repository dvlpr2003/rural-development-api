from rest_framework.routers import DefaultRouter
from.views import *

route = DefaultRouter()
route.register("login",LoginSet)
route.register("signup",SignupSet)
urlpatterns = route.urls