from rest_framework import serializers
from .models import Property
from datetime import date
class PropertySerializer(serializers.Serializer):
    class Meta:
        model = Property
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['date_listed'] = instance.date_listed
        days_on_site = (date.today() - instance.date_listed).days
        data['days_on_site'] = days_on_site
        return data