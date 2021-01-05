from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Ticket(models.Model):
    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE, related_name='tickets')
    passenger = models.ForeignKey('passengers.Passenger', on_delete=models.CASCADE, related_name='tickets')
    seat = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f'{self.ride.route.number} - {self.ride.bus.licence_plate} - {self.passenger}'
