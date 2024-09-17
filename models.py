# models.py
from django.db import models

class Ambulance(models.Model):
    size = models.CharField(max_length=50)
    location = models.CharField(max_length=255)  # Simplified for this example
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.size} Ambulance at {self.location}"

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # Simplified for this example

    def __str__(self):
        return self.name

class Booking(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    pick_up_point = models.CharField(max_length=255)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.ambulance} to {self.hospital} at {self.date_time}"
