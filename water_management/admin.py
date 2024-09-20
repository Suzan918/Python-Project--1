# water_management/admin.py

from django.contrib import admin
from .models import WaterSource, IrrigationSystem, Crop, PrecisionAgricultureMetric

admin.site.register(WaterSource)
admin.site.register(IrrigationSystem)
admin.site.register(Crop)
admin.site.register(PrecisionAgricultureMetric)
