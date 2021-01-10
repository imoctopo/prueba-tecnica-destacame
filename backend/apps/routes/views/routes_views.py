from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Route
from ..serializers import RouteSerializer
from ...buses.models import Bus
from ...buses.serializers import BusSerializer
from ...rides.serializers import TicketDetailSerializer, RideDetailSerializer
from ...rides.views import TicketViewSet, RideViewSet


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    @action(detail=True, methods=['GET'])
    def buses(self, request, pk):
        route = self.get_object()
        percent = request.query_params.get('percent', 0)
        rides = route.rides.annotate(tickets_sold_percent=Count('tickets') * 10)
        if percent and percent.isnumeric():
            rides = rides.filter(tickets_sold_percent__gte=percent)
        buses_ = Bus.objects.filter(rides__in=rides).distinct()
        return Response(BusSerializer(buses_, many=True).data)


class RouteRideViewSet(RideViewSet):
    serializer_class = RideDetailSerializer
    remove_fields = ['route']

    def get_queryset(self):
        route = self.route
        return route.rides


class RouteRideTicketViewSet(TicketViewSet):
    serializer_class = TicketDetailSerializer
    remove_fields = ['ride']

    def get_queryset(self):
        ride = self.ride
        return ride.tickets
