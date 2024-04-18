from django.urls import path
from . import views

urlpatterns = [
    path("", views.random_int, name="random_int")   
]