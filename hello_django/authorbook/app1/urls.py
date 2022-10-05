from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.add),
    path('books/<int:id>',views.viewbook),
    path('authbook/<int:id>',views.authbook),
    path('author', views.index3),
    path('addauthor', views.add2),
    path('authors/<int:id>',views.viewauthor),
    path('authbook/<int:id>',views.authbook)
]