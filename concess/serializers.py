from rest_framework import serializers
from .models import Concessionnaire, Vehicule




class ConcessionnaireSerializer(serializers.ModelSerializer):
# Ne pas exposer le champ 'siret' via l'API
    class Meta:
        model = Concessionnaire
fields = ['id', 'nom']




class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
fields = ['id', 'concessionnaire', 'type', 'marque', 'chevaux', 'prix_ht']
read_only_fields = ['concessionnaire']