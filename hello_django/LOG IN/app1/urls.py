from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create' , views.create),
    path('success' , views.success),
    path('login',views.login),
    path('delete' , views.logout),
]