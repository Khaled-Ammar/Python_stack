from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.root),
    path('shows/news', views.indexAdd),
    path('addProcess',views.add),
    path('shows/<int:id>',views.showDetail)
]