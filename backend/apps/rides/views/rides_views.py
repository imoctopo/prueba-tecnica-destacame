from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Ticket, Ride
from ..serializers import TicketSerializer, RideSerializer, TicketDetailSerializer
from ...routes.models import Route


class RideViewSet(viewsets.GenericViewSet):
    remove_fields = list()

    def get_queryset(self):
        return Ride.objects.all()

    @property
    def route(self):
        return get_object_or_404(Route, pk=self.kwargs['route_pk'])

    @property
    def ride(self) -> Ride:
        return get_object_or_404(Ride, pk=self.kwargs['pk'], route_id=self.kwargs['route_pk'])

    def create(self, request, **kwargs):
        route = self.route
        serializer = RideSerializer(data={**request.data, 'route': route.id})
        serializer.is_valid(raise_exception=True)
        ride = serializer.save(route=route)
        return Response(self.get_serializer(ride, remove_fields=self.remove_fields).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, **kwargs):
        ride = self.ride
        return Response(self.get_serializer(ride, remove_fields=self.remove_fields).data)

    def update(self, request, **kwargs):
        serializer = RideSerializer(instance=self.ride, data={**request.data, 'route': self.route.id})
        serializer.is_valid(raise_exception=True)
        ride = serializer.save()
        return Response(self.get_serializer(ride, remove_fields=self.remove_fields).data)

    def destroy(self, request, **kwargs):
        self.ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True, remove_fields=self.remove_fields).data)

    @action(detail=True, methods=['GET'], url_path='free-seats')
    def free_seats(self, request, **kwargs):
        seats = {x for x in range(1, 11)}
        occupied_seats = {x['seat'] for x in self.ride.tickets.values('seat')}
        return Response(sorted(seats - occupied_seats))


class TicketViewSet(viewsets.GenericViewSet):
    serializer_class = TicketSerializer
    remove_fields = list()

    def get_queryset(self):
        return Ticket.objects.all()

    @property
    def ride(self) -> Ride:
        return get_object_or_404(Ride, pk=self.kwargs.get('ride_pk')) if 'ride_pk' in self.kwargs else None

    @property
    def ticket(self):
        return get_object_or_404(Ticket, pk=self.kwargs['pk'], ride_id=self.kwargs['ride_pk'])

    def create(self, request, **kwargs):
        ride = self.ride
        data = dict(request.data)
        data.update({'ride': ride.id} if ride else {})
        serializer = TicketSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save(ride=serializer.validated_data['ride'])
        return Response(self.get_serializer(ticket, remove_fields=self.remove_fields).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, **kwargs):
        ticket = self.ticket
        return Response(self.get_serializer(ticket, remove_fields=self.remove_fields).data)

    def update(self, request, **kwargs):
        ticket: Ticket = self.get_object()
        serializer = TicketSerializer(instance=ticket, data={**request.data, 'ride': self.ride.id})
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        return Response(self.get_serializer(ticket, remove_fields=self.remove_fields).data)

    def destroy(self, request, **kwargs):
        self.ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True, remove_fields=self.remove_fields).data)


class RideTicketViewSet(TicketViewSet):
    serializer_class = TicketDetailSerializer
    remove_fields = ['ride']

    def get_queryset(self):
        ride = get_object_or_404(Ride, pk=self.kwargs['ride_pk'])
        return ride.tickets
