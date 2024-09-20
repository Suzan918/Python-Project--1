# water_management/models.py

from django.db import models
from django.utils import timezone

class WaterSource(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., liters or cubic meters
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class GardeningSchedule(models.Model):
    plant_name = models.CharField(max_length=100)
    plant_countdown_days = models.IntegerField(default=7)
    last_datetime = models.DateTimeField(default=timezone.now)
    next_datetime = models.DateTimeField(default=timezone.now)
    category = models.CharField(default='low',max_length=50, choices=[('low', 'low'), ('moderate', 'moderate'), ('high', 'high')], null=False)
    default_days = models.IntegerField(default=0)
    gnumber = models.IntegerField(default=2)

    def save(self, *args, **kwargs):
        if self.category == 'low':
           self.gnumber =1
           self.default_days = 7
        if self.category == 'moderate':
           self.gnumber =2
           self.default_days = 7
        if self.category == 'high':
           self.gnumber = 10
           self.default_days = 14
        
        
        # Ensure countdown days and gnumber are positive
        if self.plant_countdown_days < 0:
            raise ValidationError('Countdown days must be a positive number')
        if self.gnumber < 0:
            raise ValidationError('Gnumber must be a positive number')

        


        # Auto-calculate next_datetime based on default_days
        self.next_datetime = self.last_datetime + timezone.timedelta(days=self.default_days)
        
        super(GardeningSchedule, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.plant_name} ({self.category})"
        
class IrrigationSystem(models.Model):
    name = models.CharField(max_length=100)
    water_source = models.ForeignKey(WaterSource, on_delete=models.CASCADE)
    efficiency = models.DecimalField(max_digits=5, decimal_places=2)  # Efficiency percentage
    status = models.CharField(max_length=50, choices=[('operational', 'Operational'), ('maintenance', 'Maintenance')])

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    optimal_water_level = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., mm of water per day

    def __str__(self):
        return self.name


class PrecisionAgricultureMetric(models.Model):
    irrigation_system = models.ForeignKey(IrrigationSystem, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2)  # Soil moisture percentage
    rainfall = models.DecimalField(max_digits=5, decimal_places=2)  # Rainfall in mm
    irrigation_amount = models.DecimalField(max_digits=5, decimal_places=2)  # Water used in irrigation in liters
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metric for {self.crop.name} on {self.timestamp}"


class FarmingUnit(models.Model):
    req = models.CharField(max_length=20, unique=True,default='UNKNOWN_REQNO')  # Example: COCALP00001
    town = models.CharField(max_length=100,default='none')
    no = models.PositiveIntegerField(default=0)  # Example: 1 or 2
    type = models.CharField(max_length=100, default='Farming units/enterprise')
    district = models.CharField(max_length=100,default='none')
    amount = models.PositiveIntegerField(default=0.0)

    def __str__(self):
        return f'{self.reqno} - {self.town}'
