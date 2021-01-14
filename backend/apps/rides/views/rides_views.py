from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Ticket, Ride
from ..serializers import TicketSerializer, RideSerializer, RideDetailSerializer, TicketDetailSerializer
from ...common.pagination import DefaultPagination


class RideViewSet(viewsets.GenericViewSet):
    serializer_class = RideDetailSerializer
    pagination_class = DefaultPagination

    def paginate_queryset(self, queryset):
        if 'all' in self.request.query_params:
            return None
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        return Ride.objects.all()

    def create(self, request):
        serializer = RideSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ride = serializer.save()
        return Response(self.get_serializer(ride).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        ride = self.get_object()
        return Response(self.get_serializer(ride).data)

    def update(self, request, pk):
        serializer = RideSerializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        ride = serializer.save()
        return Response(self.get_serializer(ride).data)

    def destroy(self, request, pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(self.get_serializer(self.get_queryset(), many=True).data)

    @action(detail=True, methods=['GET'], url_path='free-seats')
    def free_seats(self, request, **kwargs):
        return Response(self.get_object().free_seats)


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
