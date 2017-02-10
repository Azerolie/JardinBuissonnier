#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404

from contact.forms import ContactForm

# return redirect("https://www.djangoproject.com")


def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire

            nom = form.cleaned_data['nom']
            mail = form.cleaned_data['mail']
            numero = form.cleaned_data['numero']
            message = form.cleaned_data['message']

            try:
                send_mail("Message du jardin buissonnier de %s" % nom, message, mail, ['emma.prudent@laposte.net'])
            except BadHeaderError:
                print("marche pas")
                return HttpResponse('Invalid header found.')
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide
        
    return render(request, 'contact/contact_accueil.html',locals())

