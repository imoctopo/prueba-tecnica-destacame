from django.db import models

from ...drivers.models import Driver


class Bus(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, blank=True, null=True)
    licence_plate = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.licence_plate

    def save(self, *args, **kwargs):
        self.licence_plate = str(self.licence_plate).upper()
        super().save(*args, **kwargs)
