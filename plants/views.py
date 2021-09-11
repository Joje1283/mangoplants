from django.shortcuts import render
from .models import Plant


def plant_list(requeset):
    plants = Plant.objects.all()
    return render(requeset, 'plants/plant_list.html', {'plants': plants})
