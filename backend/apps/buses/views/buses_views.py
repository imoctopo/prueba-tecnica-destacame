from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Bus
from ..serializers import BusSerializer
from ...common.pagination import DefaultPagination
from ...rides.serializers import RideDetailSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    pagination_class = DefaultPagination

    def paginate_queryset(self, queryset):
        if 'all' in self.request.query_params:
            return None
        return super().paginate_queryset(queryset)


class BusRidesViewSet(viewsets.GenericViewSet):
    serializer_class = RideDetailSerializer

    def get_queryset(self):
        bus = get_object_or_404(Bus, pk=self.kwargs['bus_pk'])
        return bus.rides

    def retrieve(self, request, **kwargs):
        return Response(self.get_serializer(self.get_object()).data)

    def list(self, request, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True, remove_fields=['bus']).data)
