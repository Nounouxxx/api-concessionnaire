from django.db import models
from django.core.exceptions import ValidationError




def validate_siret(value):
    if not isinstance(value, str) or len(value) != 14 or not value.isdigit():
        raise ValidationError('Le SIRET doit être une chaîne de 14 chiffres.')




class Concessionnaire(models.Model):
    nom = models.CharField(max_length=64)
siret = models.CharField(max_length=14, validators=[validate_siret])


def __str__(self):
    return self.nom




class Vehicule(models.Model):
    TYPE_CHOICES = (
('moto', 'moto'),
('auto', 'auto'),
)
concessionnaire = models.ForeignKey(Concessionnaire, related_name='vehicules', on_delete=models.CASCADE)
type = models.CharField(max_length=10, choices=TYPE_CHOICES)
marque = models.CharField(max_length=64)
chevaux = models.IntegerField()
prix_ht = models.FloatField()


def __str__(self):
    return f"{self.marque} ({self.type})"