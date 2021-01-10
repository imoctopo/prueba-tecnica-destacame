from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import RideViewSet, TicketViewSet, RideTicketViewSet

app_name = 'rides'

router = SimpleRouter(trailing_slash=False)
router.register(r'rides', RideViewSet, basename='rides')
router.register(r'tickets', TicketViewSet, basename='tickets')

ride_router = NestedSimpleRouter(router, r'rides', lookup='ride')
ride_router.register(r'tickets', RideTicketViewSet, basename='ride_tickets')

urlpatterns = router.urls + ride_router.urls
