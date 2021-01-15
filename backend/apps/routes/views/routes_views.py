from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Route
from ..serializers import RouteSerializer
from ...buses.models import Bus
from ...buses.serializers import BusSerializer
from ...common.pagination import DefaultPagination


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
    pagination_class = DefaultPagination

    def paginate_queryset(self, queryset):
        if 'all' in self.request.query_params:
            return None
        return super().paginate_queryset(queryset)

    @action(detail=True, methods=['GET'])
    def buses(self, request, pk):
        route = self.get_object()
        percent = request.query_params.get('percent', 0)
        rides = route.rides.annotate(tickets_sold_percent=Count('tickets') * 10)
        if percent and percent.isnumeric():
            rides = rides.filter(tickets_sold_percent__gte=percent)
        buses_ = Bus.objects.filter(rides__in=rides).distinct()
        return Response(BusSerializer(buses_, many=True).data)
