from rest_framework import viewsets
from ..models import Ticket, Ride
from ..serializers import TicketSerializer, RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
