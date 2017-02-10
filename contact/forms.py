from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=20, label="Nom, Prénom")
    mail = forms.EmailField(label="Adresse email")
    numero = forms.CharField(max_length=10, label="Numéro de téléphone", required=False)
    message = forms.CharField(widget=forms.Textarea)
