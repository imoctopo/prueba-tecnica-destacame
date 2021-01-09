from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} {self.last_name}'
