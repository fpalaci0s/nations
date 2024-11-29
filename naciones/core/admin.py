from django.contrib import admin
from .models import Nation, Building, NationBuilding, Technology, NationTechnology

# Register your models here.

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'food', 'water', 'money', 'wood', 'stone', 'turn')
    search_fields = ('name', 'user__username')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_cost', 'water_cost', 'money_cost', 'wood_cost', 'stone_cost')
    search_fields = ('name',)

@admin.register(NationBuilding)
class NationBuildingAdmin(admin.ModelAdmin):
    list_display = ('nation', 'building', 'quantity')
    search_fields = ('nation__name', 'building__name')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_turn')
    search_fields = ('name',)

@admin.register(NationTechnology)
class NationTechnologyAdmin(admin.ModelAdmin):
    list_display = ('nation', 'technology')
    search_fields = ('nation__name', 'technology__name')
