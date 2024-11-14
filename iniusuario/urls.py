from django.urls import path,include
from iniusuario import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logaut/', views.exit, name='exit'),
    path('registro/', views.Registro, name='Registro'),
    path('login/', views.CustomLoginView.as_view(), name='Login')
]
