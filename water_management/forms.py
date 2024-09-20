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
        "plant_name" : forms.TextInput(attrs={"placeholder":"plant name"}),
        'default_days': forms.HiddenInput(),
        'plant_countdown_days': forms.HiddenInput(),
        'last_datetime': forms.HiddenInput(),
        'next_datetime': forms.HiddenInput(),
        'gnumber': forms.HiddenInput(),
         'category': forms.Select(attrs={'class': 'form-control',"placeholder":"plant_countdown_days"}),
        }


class PlantSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search for a plant',
        })
    )
