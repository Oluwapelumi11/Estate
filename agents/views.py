from django.shortcuts import render
from rest_framework import generics
from .models import Agent
from .serializer import AgentSerializer


# Create your views here.

class AgentListAPIView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
