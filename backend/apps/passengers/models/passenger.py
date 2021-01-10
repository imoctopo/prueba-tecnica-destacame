from ...common.models import Person
from ...rides.models import Ride


class Passenger(Person):
    @property
    def rides(self):
        tickets = self.tickets.all()
        rides_ = Ride.objects.filter(tickets__in=tickets).distinct()
        return rides_
