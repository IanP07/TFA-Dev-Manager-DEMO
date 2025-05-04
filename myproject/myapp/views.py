from django.shortcuts import render, redirect
from django.http import HttpResponse    
from django.template import loader
from .models import Devices
from django.db.models import Q


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

    search_query = request.GET.get('search')

    if search_query:
        queryset = queryset.filter(
            Q(device_name__icontains=search_query) |
            Q(device_brand__icontains=search_query) |
            Q(room__icontains=search_query) |
            Q(device_type__icontains=search_query) |
            Q(device_os__icontains=search_query)
        )

   
    context = {'device': queryset} # Returns device saved under 'queryset' if it has been searched
    return render(request, 'device_list.html', context)

def add_device(request):
    if request.method == 'POST':
        data = request.POST

        device_name = data.get('device_name')
        device_brand = data.get('device_brand')
        room = data.get('room')
        device_type = data.get('device_type')
        device_os = data.get('device_os')

        Devices.objects.create( # Adds new device to Devices model, which is displayed in the def devices function. 
            device_name = device_name,
            device_brand = device_brand,
            room = room,
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
        room = data.get('room')
        device_type = data.get('device_type')
        device_os = data.get('device_os')

        queryset.device_name = device_name
        queryset.device_brand = device_brand
        queryset.room = room
        queryset.device_type = device_type
        queryset.device_os = device_os

        queryset.save()
        return redirect('device_list')

    context = {
        'device': queryset
    }

    return render(request, 'update_device.html', context)
