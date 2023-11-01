from django.urls import path
from .views import login, register, logout, index, adminRegister, adminLogin

app_name = 'User'
urlpatterns = [
    path('index/', index),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('adminLogin/', adminLogin),
    path('adminRegister/', adminRegister),
]