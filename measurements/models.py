from django.db import models

# Create your models here.

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"
class Quarantine(models.Model):
    Facility = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    Rank = models.IntegerField(max_length=10)
    Longitude = models.IntegerField(max_length=200)
    Latitude = models.IntegerField(max_length=200)

    def __str__(self):
        return f"Quarantine centre {self.Facility} has Rank {self.Rank}"
class city(models.Model):
    city = models.CharField(max_length=200)
    rank = models.IntegerField(max_length=200)
    Place = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.city








