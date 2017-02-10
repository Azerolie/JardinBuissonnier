from django.shortcuts import render

# Create your views here.#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


# return redirect("https://www.djangoproject.com")

   
def jardin_accueil(request):
    return render(request, 'jardins/jardin_accueil.html')


