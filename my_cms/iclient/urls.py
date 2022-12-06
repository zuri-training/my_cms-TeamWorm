
from django.urls import path
from . import views

app_name = 'iclient'
urlpatterns = [
    path('', views.index, name='index')
]


