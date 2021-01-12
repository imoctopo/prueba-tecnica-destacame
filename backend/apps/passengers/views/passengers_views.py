from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from ..models import Passenger
from ..serializers import PassengerSerializer
from ...common.pagination import DefaultPagination
from ...rides.serializers import TicketDetailSerializer, RideDetailSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    pagination_class = DefaultPagination


class PassengerRideViewSet(viewsets.GenericViewSet):
    serializer_class = RideDetailSerializer

    def get_queryset(self):
        passenger = get_object_or_404(Passenger, pk=self.kwargs['passenger_pk'])
        return passenger.rides

    def retrieve(self, request, **kwargs):
        return Response(self.get_serializer(self.get_object()).data)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)


class PassengerTicketViewSet(viewsets.GenericViewSet):
    serializer_class = TicketDetailSerializer

    def get_queryset(self):
        passenger = get_object_or_404(Passenger, pk=self.kwargs['passenger_pk'])
        return passenger.tickets

    def retrieve(self, request, **kwargs):
        return Response(self.get_serializer(self.get_object(), remove_fields=['passenger']).data)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True, remove_fields=['passenger']).data)
