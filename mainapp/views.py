from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    return HttpResponse("Welcome!")

def second_page(request):
    return HttpResponse("About")

def profile_page(request):
    return HttpResponse("Profile")

