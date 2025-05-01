from django.db import models
# Create your models here.

os_options = (
        ('windows10','WIN10'), # Second values are ones that are displayed in html
        ('windows11', 'WIN11'),
        ('ChromeOS','CHROMEOS'),
        ('Linux','LINUX'),
        ('macOS','MACOS'),
        ('other', 'OTHER')
    )

brands = (
    ('laptop', 'LAPTOP'),
    ('desktop', 'DESKTOP'),
    ('projector', 'PROJECTOR'),
    ('TV', 'TV'),
    ('Other', 'OTHER')
)
class Devices(models.Model):
    device_name = models.CharField(max_length=300)
    device_brand = models.CharField(max_length=300)
    device_type = models.CharField(max_length=100, choices=brands)
    device_os = models.CharField(max_length=300, choices=os_options)