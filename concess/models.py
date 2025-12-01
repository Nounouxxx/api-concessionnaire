from django.db import models
from django.core.exceptions import ValidationError

def validate_siret(value):
    if len(value) != 14 or not value.isdigit():
        raise ValidationError("Le SIRET doit faire exactement 14 chiffres.")
    
TYPE_CHOICES = [
    ('moto', 'moto'),
    ('auto', 'auto'),
]

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=64)
    siret = models.CharField(max_length=14, validators=[validate_siret])

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=64)
    chevaux = models.IntegerField()
    prix_ht = models.FloatField()
    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name="vehicules"
    )

    def __str__(self):
        return f"{self.marque} ({self.type})"
