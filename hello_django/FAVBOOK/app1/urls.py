from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create' , views.create),
    path('success' , views.success),
    path('login',views.login),
    path('delete' , views.logout),
    path('MainPage' , views.mainpage),
    path('fav' , views.fav),
    path('books/<id>' , views.BookDetails),
    path('addtofav/<id>' , views.addToFav),
    path('remove/<id>' , views.remove),
    path('deleteUpdate/<id>' , views.DeleteUpdate),
    path('main',views.back),
]