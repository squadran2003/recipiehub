from django.db import models
from django.contrib.auth.models import User

class Recipie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.name
    

class Ingredient(models.Model):
    recipie = models.ForeignKey(Recipie, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Instruction(models.Model):
    recipie = models.ForeignKey(Recipie, related_name='instructions', on_delete=models.CASCADE)
    order = models.IntegerField(default=-1)
    instruction_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.instruction_text



