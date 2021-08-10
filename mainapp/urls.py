from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_page),
    path('about/', views.second_page),
    path('', views.landing_page),
]
