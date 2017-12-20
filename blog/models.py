from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.CharField(max_length=20000)
    date_creation = models.DateField()

    def __str__(self):
        return self.titre