from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Ticket, Ride
from ..serializers import TicketSerializer


class TicketViewSet(viewsets.GenericViewSet):
    serializer_class = TicketSerializer
    parent_model = Ride

    def get_queryset(self):
        return self.ride.tickets.all()

    @property
    def ride(self) -> Ride:
        return get_object_or_404(Ride, pk=self.kwargs['ride_pk'])

    @property
    def ticket(self):
        return get_object_or_404(Ticket, pk=self.kwargs['pk'], ride_id=self.kwargs['ride_pk'])

    def create(self, request, **kwargs):
        ride = self.ride
        serializer = TicketSerializer(data={**request.data, 'ride': ride.id})
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save(ride=ride)
        return Response(self.get_serializer(ticket).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, **kwargs):
        ticket = self.ticket
        return Response(self.get_serializer(ticket).data)

    def update(self, request, **kwargs):
        ticket: Ticket = self.get_object()
        serializer = TicketSerializer(instance=ticket, data={**request.data, 'ride': self.ride.id})
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        return Response(self.get_serializer(ticket).data)

    def destroy(self, request, **kwargs):
        self.ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)
