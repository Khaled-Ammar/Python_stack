from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create' , views.create),
    path('success' , views.success),
    path('login',views.login),
    path('delete' , views.logout),
    path('toindex1',views.index1),
    path('toall',views.toall),
    path('plans/' , views.table),
    path('plans/create/',views.details),
    path('plans/<id>/edit' ,views.edit),
    path('plans/<id>/update',views.update),
    path('plans/<id>/destroy',views.destroy),
    path('toindex1' ,views.toindex1),
    path('show/<int:id>',views.treeshow),
    path('mytree',views.my),
]
