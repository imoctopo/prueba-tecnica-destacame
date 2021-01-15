from django.db import models
from django.db.models import Count, Avg


class Route(models.Model):
    number = models.CharField(unique=True, max_length=3)
    starting_address = models.CharField(max_length=100)
    ending_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}'

    @property
    def passengers_average(self):
        avg = self.rides.annotate(tickets_sold=Count('tickets'))
        avg = avg.aggregate(avg=Avg('tickets_sold'))
        return round(avg['avg'], 1) if avg['avg'] else 0

    def save(self, *args, **kwargs):
        self.number = str(self.number).upper()
        super().save(*args, **kwargs)
