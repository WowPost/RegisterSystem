from django.urls import path
from  Users import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users/', views.users, name="users_listing")
]
