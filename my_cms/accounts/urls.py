from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    
]

#TODO: /login
#TODO: /signup
#TODO: /forgot_password