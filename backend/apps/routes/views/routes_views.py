from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from ..models import Route
from ..serializers import RouteSerializer
from ...rides.models import Ride
from ...rides.serializers import TicketDetailSerializer, RideDetailSerializer
from ...rides.views import TicketViewSet, RideViewSet


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class RouteRideViewSet(RideViewSet):
    serializer_class = RideDetailSerializer
    remove_fields = ['route']

    def get_queryset(self):
        route = get_object_or_404(Route, id=self.kwargs['route_pk'])
        return route.rides


class RouteRideTicketViewSet(TicketViewSet):
    serializer_class = TicketDetailSerializer
    remove_fields = ['ride']

    def get_queryset(self):
        ride = get_object_or_404(Ride, pk=self.kwargs['ride_pk'], route_id=self.kwargs['route_pk'])
        return ride.tickets
