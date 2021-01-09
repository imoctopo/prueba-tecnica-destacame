from rest_framework import viewsets
from ..models import Ticket, Ride
from ..serializers import TicketSerializer, RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    serializer_class = RideSerializer

    def get_queryset(self):
        return Ride.objects.all()
