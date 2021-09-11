from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_list.html', {'plants': plants})


def plant_create(request):
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:plant_list')
    else:
        plant_form = PlantForm()
    return render(request, 'plants/plant_form.html', {'form': plant_form})
