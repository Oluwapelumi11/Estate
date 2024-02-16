from rest_framework import serializers
from .models import Property,Image
from datetime import date


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')  

class PropertySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['date_listed'] = instance.date_listed
        days_on_site = (date.today() - instance.date_listed).days
        data['days_on_site'] = days_on_site + 1
        return data