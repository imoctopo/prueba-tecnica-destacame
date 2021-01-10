from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import BusViewSet, BusRidesViewSet

app_name = 'buses'

router = SimpleRouter(trailing_slash=False)
router.register(r'buses', BusViewSet, basename='buses')

bus_router = NestedSimpleRouter(router, r'buses', lookup='bus')
bus_router.register(r'rides', BusRidesViewSet, basename='bus_rides')

urlpatterns = router.urls + bus_router.urls
