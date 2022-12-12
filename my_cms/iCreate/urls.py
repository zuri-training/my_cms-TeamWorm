
from django.urls import path
from . import views

app_name = 'iCreate'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('recover-pw', views.recover_pw, name='recover-pw'),
]


