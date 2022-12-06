
from django.urls import path
from . import views

app_name = 'iCreate'
urlpatterns = [
    path('', views.index, name='index')
]


