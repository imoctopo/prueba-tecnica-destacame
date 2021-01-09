from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import RouteViewSet, RouteRideViewSet, RouteRideTicketViewSet

app_name = 'routes'

router = SimpleRouter(trailing_slash=False)
router.register(r'routes', RouteViewSet, basename='routes')

routes_router = NestedSimpleRouter(router, r'routes', lookup='route')
routes_router.register(r'rides', RouteRideViewSet, basename='route_rides')

routes_rides_router = NestedSimpleRouter(routes_router, 'rides', lookup='ride')
routes_rides_router.register(r'tickets', RouteRideTicketViewSet, basename='route_ride_tickets')

urlpatterns = router.urls + routes_router.urls + routes_rides_router.urls
