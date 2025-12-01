# Corrected initial migration
from django.db import migrations, models
import django.db.models.deletion
import concess.models


class Migration(migrations.Migration):


    initial = True


    dependencies = []


    operations = [
    migrations.CreateModel(
        name='Concessionnaire',
        fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('nom', models.CharField(max_length=64)),
            ('siret', models.CharField(max_length=14)),
        ],   # ← ICI : fermeture correcte du fields=[
    ),      # ← fermeture du CreateModel
    migrations.CreateModel(
        name='Vehicule',
        fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('type', models.CharField(max_length=10)),
            ('marque', models.CharField(max_length=64)),
            ('chevaux', models.IntegerField()),
            ('prix_ht', models.FloatField()),
            ('concessionnaire',
                 models.ForeignKey(to='concess.Concessionnaire', on_delete=models.CASCADE)),
        ],
    ),
] 