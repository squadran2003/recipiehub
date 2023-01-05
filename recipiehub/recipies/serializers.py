from rest_framework import serializers
from .models import Recipie,Ingredient, Instruction

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','recipie', 'name', 'created_at',]


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id','recipie', 'order', 'instruction_text', 'created_at']


class RecipieSerialier(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = ['id','user', 'name', 'created_at',]
    

    def create(self, validated_data):
        ingredients = self.context.get('ingredients',None)
        instructions = self.context.get('instructions',None)
        if not ingredients:
            raise serializers.ValidationError(
                "You must pass ingrediates when creating a recipie"
            )
        if not instructions:
            raise serializers.ValidationError(
                "You must pass instructions when creating a recipie"
            )
        recipie = Recipie.objects.create(**validated_data)
        for ingredient_name in ingredients:
            Ingredient.objects.create(recipie=recipie,name=ingredient_name)
        for instruction in instructions:
            Instruction.objects.create(
                recipie=recipie,instruction_text=instruction.get('instruction_text'),
                order=instruction.get('order')
            )
        return recipie
    
    def validate_name(self, name):
        user_id = self.context['user_id']
        try:
            Recipie.objects.get(name=name.lower(),user=user_id)
        except Recipie.DoesNotExist:
            return name
        else:
            raise serializers.ValidationError("recipie by this user already exists")
            

class RecipieDetailSerialier(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    instructions = InstructionSerializer(many=True, read_only=True)
    class Meta:
        model = Recipie
        fields = ['id','user', 'name', 'ingredients', 'instructions', 'created_at',]

