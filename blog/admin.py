from django.contrib import admin
from blog.models import Categorie, Article, Jardin, Legume

       
class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'date','categorie','apercu_contenu')
   list_filter    = ('categorie',)
   date_hierarchy = 'date'
   ordering       = ('date',)
   search_fields  = ('titre', 'contenu')
   fields = ('titre', 'categorie', 'contenu','photo')
   
   def apercu_contenu(self, article):
    """ 
    Retourne les 40 premiers caractères du contenu de l'article. S'il
    y a plus de 40 caractères, il faut ajouter des points de suspension.
    """
    text = article.contenu[0:40]
    if len(article.contenu) > 40:
        return '%s...' % text
    else:
        return text
        
   apercu_contenu.short_description = 'Aperçu du contenu'     

class LegumeAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'prix','jardin','disponible','description')
   list_filter    = ('jardin','disponible')
   ordering       = ('nom',)
   search_fields  = ('nom', 'description')
   fields = ('nom','jardin','prix', 'description','photo','disponible')
   
   def apercu_contenu(self, article):
    """ 
    Retourne les 40 premiers caractères du contenu de l'article. S'il
    y a plus de 40 caractères, il faut ajouter des points de suspension.
    """
    text = article.contenu[0:40]
    if len(article.contenu) > 40:
        return '%s...' % text
    else:
        return text
        
   apercu_contenu.short_description = 'Aperçu du contenu' 
      
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Jardin)
admin.site.register(Legume,LegumeAdmin)
