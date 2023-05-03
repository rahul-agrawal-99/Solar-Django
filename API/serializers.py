#   import serializers from rest_framework

from rest_framework import serializers
from .models import SolarData



class SolarDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolarData
        fields = ('Timestamp' , 'slaveId' , 'voltage' , 'current' , 'active_power' , 'reactive_power'  , 'apperant_power' , 'active_current' , 'reactive_current')
        