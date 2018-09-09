
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest

from equipment.models import Vehicle, VehicleBrand, VehicleModel

def index(request):
    vehicles = Vehicle.objects.all()
    models = VehicleModel.objects.all()

    return render(request, 'capacity_info.html', { 'vehicles' : vehicles, 'models': models})

def get_vehicles(request):
    
    model = request.GET.get('model')

    if not model:
        return HttpResponseBadRequest()

    vehicles = []

    if model == 'all':
        vehicles = Vehicle.objects.all()
    else:
        vehicles = Vehicle.objects.filter(vehicle_model = model)

    return render(request, 'capacity_table.html', {'veh': vehicles})