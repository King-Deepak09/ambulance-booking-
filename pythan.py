from django.db import models

class Ambulance(models.Model):
    size = models.CharField(max_length=50)
    location = models.PointField()  # Requires django.contrib.gis
    is_available = models.BooleanField(default=True)

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()  # Requires django.contrib.gis

class Booking(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    pick_up_point = models.CharField(max_length=255)
    date_time = models.DateTimeField()
