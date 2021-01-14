from django.db import models
from django.db.models import Count, Avg


class Route(models.Model):
    number = models.CharField(unique=True, max_length=3)
    starting_address = models.CharField(max_length=100)
    ending_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}'

    @property
    def passenger_average(self):
        avg = self.rides.annotate(tickets_sold=Count('tickets'))
        avg = avg.aggregate(avg=Avg('tickets_sold'))
        return avg['avg']

    @property
    def total_rides(self):
        return self.rides.count()

    @property
    def total_tickets(self):
        return self.rides.aggregate(total_tickets=Count('tickets'))['total_tickets']

    def save(self, *args, **kwargs):
        self.number = str(self.number).upper()
        super().save(*args, **kwargs)
