from django.contrib import admin
from .models import Categorie
from .models import Element
from .models import Commentaire

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Element)
admin.site.register(Commentaire)