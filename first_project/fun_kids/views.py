from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    categorie = Categorie.objects.all()
    return render(request, 'fun_kids/home.html', {'categorie': Categorie})


def about(request):

    return render(request, 'fun_kids/about.html')


def contact(request):

    return render(request, 'fun_kids/contact.html')


def categorie(request):
    element = Element.objects.all()
    return render(request, 'fun_kids/categorie.html', {'element': Element})