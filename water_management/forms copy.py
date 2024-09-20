# forms.py

from django import forms
from .models import GardeningSchedule

class GardeningScheduleForm(forms.ModelForm):
    class Meta:
        model = GardeningSchedule
        fields = '__all__'

        label = {
        "name" : "name",
        "plant_name " : "plant_name",
        "default_days" : "default_days",
        "plant_countdown_days" : "plant_countdown_days",
        "gnumber" : "gnumber",
         "category" : "category",
        }

        widgets ={
        "plant_name" : forms.TextInput(attrs={"placeholder":"plant_name"}),
        "default_days" : forms.TextInput(attrs={"placeholder":"plant_countdown_days"}),
         "gnumber" : forms.TextInput(attrs={"placeholder":"next_datetime"}),
        "plant_countdown_days" : forms.TextInput(attrs={"placeholder":"plant_countdown_days"}), 
         
           "category" : forms.TextInput(attrs={"placeholder":"category"}), 
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)