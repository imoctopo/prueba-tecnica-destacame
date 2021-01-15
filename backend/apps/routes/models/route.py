from django.db import models


class Route(models.Model):
    number = models.CharField(unique=True, max_length=3)
    starting_address = models.CharField(max_length=100)
    ending_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}'

    def save(self, *args, **kwargs):
        self.number = str(self.number).upper()
        super().save(*args, **kwargs)
