# water_management/views.py

from django.shortcuts import render
from .models import WaterSource
from .forms  import GardeningScheduleForm
from .forms  import PlantSearchForm
from django.shortcuts import redirect
from .models import GardeningSchedule
from django.utils import timezone


def low_list(request):
    water_plants = GardeningSchedule.objects.filter(category='low')
    return render(request, 'low_water.html', {'water_plants': water_plants})

def moderate_list(request):
    water_plants = GardeningSchedule.objects.filter(category='moderate')
    return render(request, 'moderate_water.html', {'water_plants': water_plants})

def high_list(request):
    water_plants = GardeningSchedule.objects.filter(category='high')
    return render(request, 'high_water.html', {'water_plants': water_plants})

# List all water sources
def home(request):
    water_plants = GardeningSchedule.objects.all()
    return render(request, 'awaiting.html', {'all_water_plants': water_plants})



# Create a new water source
def add_water_source(request):
    if request.method == "POST":
        form = GardeningScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GardeningScheduleForm()
    return render(request, 'add_water_source.html', {'form': form})

# views.py
def edit_water_source(request, pk):
    water_source = get_object_or_404(WaterSource, pk=pk)
    if request.method == "POST":
        form = WaterSourceForm(request.POST, instance=water_source)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WaterSourceForm(instance=water_source)
    return render(request, 'edit_water_source.html', {'form': form})

# views.py
def delete_water_source(request, pk):
    water_source = get_object_or_404(WaterSource, pk=pk)
    if request.method == "POST":
        water_source.delete()
        return redirect('home')
    return render(request, 'home/delete_water_source.html', {'water_source': water_source})

def plant_search(request):
    form = PlantSearchForm(request.GET or None)
    query = request.GET.get('query', '')
    
    if query:
        plants = GardeningSchedule.objects.filter(plant_name__icontains=query)
    else:
        plants = GardeningSchedule.objects.all()

    # Calculate the number of days remaining for each plant
    for plant in plants:
        plant.days_remaining = (plant.next_datetime - timezone.now()).days

    return render(request, 'search.html', {'form': form, 'plants': plants})