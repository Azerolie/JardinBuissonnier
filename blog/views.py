#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime
from blog.models import Article, Legume

# return redirect("https://www.djangoproject.com")

    
def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/blog_accueil.html', {'derniers_articles': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/blog_lire.html', {'article':article})

