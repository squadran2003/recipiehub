from django.contrib import admin
from .models import *


@admin.register(Recipie)
class RecipieAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipie', 'name', 'created_at')

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('order', 'recipie', 'instruction_text', 'created_at')