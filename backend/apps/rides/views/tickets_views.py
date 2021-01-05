from rest_framework import viewsets, exceptions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Ticket, Ride
from ..serializers import TicketSerializer
from ...core.errors_messages import SEAT_TAKEN, PASSENGER_ALREADY_IN_THIS_RIDE
from ...passengers.models import Passenger


class TicketViewSet(viewsets.GenericViewSet):
    serializer_class = TicketSerializer
    parent_model = Ride

    def get_queryset(self):
        return Ticket.objects.filter(ride_id=self.kwargs['ride_pk'])

    def _get_parent(self) -> Ride:
        return get_object_or_404(self.parent_model, pk=self.kwargs['ride_pk'])

    def create(self, request, ride_pk):
        ride = self._get_parent()
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the seat is taken
        if taken := ride.tickets.filter(seat=serializer.validated_data['seat']).first():
            raise exceptions.ValidationError({'seat': [SEAT_TAKEN % taken.passenger]})

        passenger: Passenger = serializer.validated_data['passenger']

        # Check if the passenger is already in this ride
        if ride.tickets.filter(passenger_id=passenger.id).exists():
            raise exceptions.ValidationError({'passenger': [PASSENGER_ALREADY_IN_THIS_RIDE]})

        ticket = serializer.save(ride=ride)
        return Response(self.get_serializer(ticket).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, ride_pk):
        ticket = get_object_or_404(Ticket, pk=pk, ride_id=ride_pk)
        return Response(self.get_serializer(ticket).data)

    def destroy(self, request, pk, ride_pk):
        ticket = get_object_or_404(Ticket, pk=pk, ride_id=ride_pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, ride_pk):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)
