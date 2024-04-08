from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members2/', views.members2, name='members2'),
]