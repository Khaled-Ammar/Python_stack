from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.add),
    path('books/<int:id>',views.viewbook),
    path('authbook/<int:id>',views.authbook)

]