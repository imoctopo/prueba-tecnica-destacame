from rest_framework import viewsets
from ..models import Driver
from ..serializers import DriverSerializer
from ...common.pagination import DefaultPagination


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    pagination_class = DefaultPagination

    def paginate_queryset(self, queryset):
        if 'all' in self.request.query_params:
            return None
        return super().paginate_queryset(queryset)
