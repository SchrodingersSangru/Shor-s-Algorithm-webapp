from django.urls import path
from shor import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('factor/', views.factor)]