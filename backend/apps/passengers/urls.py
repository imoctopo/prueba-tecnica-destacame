from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import PassengerViewSet, PassengerRideViewSet, PassengerTicketViewSet

app_name = 'passengers'

router = SimpleRouter(trailing_slash=False)
router.register(r'passengers', PassengerViewSet, basename='passengers')

passenger_router = NestedSimpleRouter(router, r'passengers', lookup='passenger')
passenger_router.register(r'rides', PassengerRideViewSet, basename='passenger_rides')
passenger_router.register(r'tickets', PassengerTicketViewSet, basename='passenger_tickets')

urlpatterns = router.urls + passenger_router.urls
