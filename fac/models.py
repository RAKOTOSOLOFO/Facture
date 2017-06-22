# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Compte(models.Model):

    devis = models.ForeignKey("Devis")



class Devis(models.Model):
    prix = models.CharField(prix,max_lenght = 30)
    Qte = models.CharField(Qte,max_lenght = 30)
    statut = models.ForeignKey("Statut")


class Statut(models.Model):
    En_cours = models.CharField(max_lenght = 30)
    Gagné = models.CharField(max_lenght = 30)
    Perdu = models.CharField(max_lenght = 30)
    archive =  models.ForeignKey("Archives")

class Archives(models.Model):
    Date = models.DateTimeFields()
