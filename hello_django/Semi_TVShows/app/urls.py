from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('shows/' , views.table),
    path('shows/create/' , views.details),
    path ('shows/<id>' , views.show),
    path('shows/<id>/edit' , views.edit),
    path('shows/<id>/update' , views.update),
    path('shows/<id>/destroy' , views.destroy),
]