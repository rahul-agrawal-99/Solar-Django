from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class SolarData(models.Model):
    Timestamp = models.DateTimeField(default=datetime.now)
    current = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    active_power = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    power_factor = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    apperant_power  =ArrayField(models.CharField(max_length=100), null=True, blank=True)
    active_energy =ArrayField(models.CharField(max_length=100), null=True, blank=True)
    voltage = ArrayField(models.CharField(max_length=100), null=True, blank=True)


    def __str__(self):
        return str(self.Timestamp)
