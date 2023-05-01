#   import serializers from rest_framework

from rest_framework import serializers
from .models import SolarData



class SolarDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolarData
        fields = '__all__'