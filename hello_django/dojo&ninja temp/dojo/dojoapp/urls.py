from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.root),
    path('addDojo', views.handle),
    path('addninja',views.handle2)

]