from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = RecipeSerializer # tell django what serializer to use

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer