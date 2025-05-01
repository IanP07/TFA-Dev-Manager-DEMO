from django.urls import path 
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('device_list/', views.devices, name="device_list"),
    path('add/', views.add_device, name="add_device"),
    path('update<int:id>/', views.update_device, name="update_device"),
    path('delete<int:id>', views.delete_device, name="delete_device"),
]