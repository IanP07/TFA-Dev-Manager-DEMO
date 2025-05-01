from django.shortcuts import render, redirect
from django.http import HttpResponse    
from django.template import loader
from .models import Devices


def login_view(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password == "1776":
            request.session["authenticated"] = True
            return redirect('/device_list/')
        else:
            return render(request, "login.html")
    return render(request, "login.html")



def devices(request):    
    if not request.session.get('authenticated'): # If user isnt logged in
        return redirect('/')
    
    queryset = Devices.objects.all()    
    if request.GET.get('search'):
        queryset = queryset.filter(
            device_name__icontains=request.GET.get('search')) # If db contains (case insensitive) the request

    context = {'device': queryset} # Returns device saved under 'queryset' if it has been searched
    return render(request, 'device_list.html', context)

def add_device(request):
    if request.method == 'POST':
        data = request.POST

        device_name = data.get('device_name')
        device_brand = data.get('device_brand')
        device_type = data.get('device_type')
        device_os = data.get('device_os')

        Devices.objects.create( # Adds new device to Devices model, which is displayed in the def devices function. 
            device_name = device_name,
            device_brand = device_brand,
            device_type = device_type,
            device_os = device_os
        )
        return redirect('device_list')
    return render(request, 'add_device.html')

def delete_device(request, id):
    queryset = Devices.objects.get(id=id) # ID parameter is used to find correct device to delete
    queryset.delete()

    return redirect('device_list')

def update_device(request, id):
    queryset = Devices.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        device_name = data.get('device_name')
        device_brand = data.get('device_brand')
        device_type = data.get('device_type')
        device_os = data.get('device_os')

        queryset.device_name = device_name
        queryset.device_brand = device_brand
        queryset.device_type = device_type
        queryset.device_os = device_os

        queryset.save()
        return redirect('device_list')

    context = {
        'device': queryset
    }

    return render(request, 'update_device.html', context)
