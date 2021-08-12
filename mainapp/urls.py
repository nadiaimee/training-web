from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('shop/food/', views.shop_food),
    path('shop/homedecor/', views.shop_home),
    path('shop/plant/', views.shop_plant),
    path('firstpage/', views.firstpage),
    path('secondpage/', views.secondpage),
    path('example/', views.example),
    path('count/<int:angka>/', views.count),
    path('sapa/<str:nama>/', views.sapa),
    path('profile/', views.profile_page),
    path('about/', views.second_page),
    path('', views.shop),
]
