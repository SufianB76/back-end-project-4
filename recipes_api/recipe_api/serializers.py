from rest_framework import serializers 
from .models import Recipe 

class RecipeSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Recipe # tell django which model to use
        fields = ('id', 'name', 'ingredients','directions', 'cooktime') # tell django which fields to include