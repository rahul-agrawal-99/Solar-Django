from django.contrib import admin

# Register your models here.

from .models import SolarData


admin.site.register(SolarData)