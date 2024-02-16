from rest_framework import serializers
from .models import Agent
class AgentSerializer(serializers.Serializer):
    class Meta:
        model = Agent
        fields = '__all__'