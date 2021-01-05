from django.db import models
from django.utils import timezone


class Ride(models.Model):
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE, related_name='rides')
    bus = models.ForeignKey('buses.Bus', on_delete=models.CASCADE, related_name='rides')
    schedule = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.route.number} - {self.bus.licence_plate}'
