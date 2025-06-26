from django.db import models
from customers.models import Customer

# Create your models here.
class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tipo de veiculo'
        verbose_name_plural = 'Tipos de veiculos'

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, blank=True, null=True, related_name='vehicles', verbose_name='Tipo do veiculo')
    license_plate = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='Marca do carro')
    model = models.CharField(max_length=50, blank=True, null=True, verbose_name='Modelo do carro')
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cor do carro')
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True, related_name='vehicles', verbose_name='Proprietario')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
    
    def __str__(self):
        return self.license_plate