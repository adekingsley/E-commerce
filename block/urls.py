from django.urls import path
from block import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produce/', views.produce, name='produce'),
    path('store/', views.store, name='store'),
    path('blank/', views.blank, name='blank'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('checkout', views.checkout, name='checkout')    
]