from django.db import models
# Create your models here.


class Voilier(models.Model):
    """Classe qui represente un voilier"""
    nom = models.CharField(max_length=100)
    nbre_equipiers = models.IntegerField()

    def __str__(self):
        return self.nom


class Navigation(models.Model):
    """
    classe qui represente une navigation
    """

    date_debut = models.DateField()
    date_fin = models.DateField()
    id_voilier = models.ForeignKey('Voilier', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_debut)
