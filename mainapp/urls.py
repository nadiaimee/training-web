from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example),
    path('count/<int:angka>/', views.count),
    path('sapa/<str:nama>/', views.sapa),
    path('profile/', views.profile_page),
    path('about/', views.second_page),
    path('', views.landing_page),
]
