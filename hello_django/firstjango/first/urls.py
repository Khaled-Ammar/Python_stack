from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi),
    path('blogs/',views.index),
    path('blogs/new/',views.new),
    path('blogs/redirect/',views.redir),
    path('blogs/<int:num>/',views.number),
    path('blogs/<int:num>/',views.edit),
    path('blogs/<int:num>/delete',views.edit),
    path('redirected_route', views.redirected_method),
]