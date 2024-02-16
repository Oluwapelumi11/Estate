from django.shortcuts import render
from rest_framework import generics
from .models import Property
from .serializer import PropertySerializer

# Create your views here.

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

