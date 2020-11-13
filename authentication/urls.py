from authentication.views import loginuser, register, logoutuser
from django.urls import path

urlpatterns = [
    path('login/', loginuser),
    path('register/', register),
    path('logout/', logoutuser),
]

