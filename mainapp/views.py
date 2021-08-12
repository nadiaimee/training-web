from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    return HttpResponse("Welcome!")

def second_page(request):
    return HttpResponse("About")

def profile_page(request):
    return HttpResponse("Profile")

def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))

def sapa(request, nama):
    return HttpResponse("Halo, "+nama+"!")

def newpage(request):
    return HttpResponse("Vision")

def example(request):
    return render(request, 'example.html')

def shop(request):
    return render(request, 'shop.html')

def shop_food(request):
    return render(request, 'shop_food.html')


def shop_home(request):
    return render(request, 'shop_home.html')


def shop_plant(request):
    return render(request, 'shop_plant.html')


def firstpage(request):
    return render(request, 'firstpage.html')


def secondpage(request):
    return render(request, 'secondpage.html')