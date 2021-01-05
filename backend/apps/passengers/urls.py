from rest_framework.routers import SimpleRouter
from .views import PassengerViewSet

app_name = 'passengers'

router = SimpleRouter(trailing_slash=False)
router.register(r'passengers', PassengerViewSet, basename='passengers')

urlpatterns = router.urls
