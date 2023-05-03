from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.

# DB_COLUMNS = ["voltage" , "current" , "active_power" , "reactive_power"  , "apperant_power" , "active_current" , "reactive_current"  ]


class SolarData(models.Model):
    Timestamp = models.DateTimeField(default=datetime.now)
    slaveId = models.IntegerField(null=True, blank=True)

    voltage = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    current = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    active_power = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    reactive_power = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    apperant_power = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    active_current =ArrayField(models.CharField(max_length=100), null=True, blank=True)
    reactive_current =ArrayField(models.CharField(max_length=100), null=True, blank=True)


    def __str__(self):
        return str(self.Timestamp)
