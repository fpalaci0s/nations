from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Modelo para los recursos de cada nación
class Nation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="nation")
    name = models.CharField(max_length=100, unique=True)
    food = models.PositiveIntegerField(default=0)
    water = models.PositiveIntegerField(default=0)
    money = models.PositiveIntegerField(default=0)
    wood = models.PositiveIntegerField(default=0)
    stone = models.PositiveIntegerField(default=0)
    turn = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def pass_turn(self):
        self.turn += 1
        self.food = max(self.food - 5, 0)  # Ejemplo: consumir comida por turno
        self.save()

# Modelo para el edificio
class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    food_cost = models.PositiveIntegerField(default=0)
    water_cost = models.PositiveIntegerField(default=0)
    money_cost = models.PositiveIntegerField(default=0)
    wood_cost = models.PositiveIntegerField(default=0)
    stone_cost = models.PositiveIntegerField(default=0)
    effect = models.TextField(help_text="Descripción del efecto del edificio")

    def __str__(self):
        return self.name

# Modelo para edificios construidos por una nación
class NationBuilding(models.Model):
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name="buildings")
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.building.name} - {self.nation.name}"

# Modelo para tecnología
class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    required_turn = models.PositiveIntegerField(default=1)  # Turnos necesarios para desbloquear

    def __str__(self):
        return self.name

# Tecnologías desbloqueadas por la nación
class NationTechnology(models.Model):
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name="technologies")
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technology.name} - {self.nation.name}"
