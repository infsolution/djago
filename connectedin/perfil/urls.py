from django.urls import path
from . import views

urlpatterns = [
    path('perfil/',views.index, name='index'),
    ]
