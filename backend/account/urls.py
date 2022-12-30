from django.urls import path
from . import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# from account.views import (
# 	home_screen_view
# )

from account.views import (
    register_view,

)

app_name = 'account'




urlpatterns = [
    path('login/', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('register/', register_view, name="register"),
    path('recover-pw/', views.recover_pw, name='recover-pw'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)