from django.db import models
# Create your models here.


class Commentaire(models.Model):
    id_Commentaire = models.BigAutoField(primary_key=True)
    Commentaire = models.TextField(max_length=2500)
    Email = models.EmailField(max_length=50)
    Nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Email


class Categorie(models.Model):
    id_Categorie = models.BigAutoField(primary_key=True)
    Nom_Categorie = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Nom_Categorie


class Element(models.Model):
    id_Element = models.BigAutoField(primary_key=True)
    Nom_Element = models.CharField(max_length=50, unique=True)
    categorie = models.ForeignKey(Categorie,related_name='Elements', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.Nom_Element