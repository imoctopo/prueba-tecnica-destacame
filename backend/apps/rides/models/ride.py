from django.db import models
from django.utils import timezone

from ...buses.models import Bus
from ...routes.models import Route


class Ride(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='rides')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='rides')
    schedule = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'[{self.id}]: {self.route.number} - {self.bus.licence_plate}'

    @property
    def free_seats(self):
        seats = {x for x in range(1, 11)}
        occupied_seats = {x['seat'] for x in self.tickets.values('seat')}
        return sorted(seats - occupied_seats)
