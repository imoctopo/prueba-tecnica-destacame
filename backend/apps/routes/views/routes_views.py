from rest_framework import viewsets

from ..models import Route
from ..serializers import RouteSerializer
from ...rides.views import TicketViewSet, RideViewSet


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class RouteRideViewSet(RideViewSet):
    pass


class RouteRideTicketViewSet(TicketViewSet):
    pass
