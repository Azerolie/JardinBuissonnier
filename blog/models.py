from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
        
        
class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    photo = models.ImageField()
    categorie = models.ForeignKey('Categorie')


    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre

class Jardin(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
        
               
        
class Legume(models.Model):
    nom = models.CharField(max_length=30)
    photo = models.ImageField()
    jardin = models.ForeignKey('Jardin')
    prix = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Prix au kilo")
    disponible = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom
        
        
