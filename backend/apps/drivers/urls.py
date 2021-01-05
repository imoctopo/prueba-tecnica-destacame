from rest_framework.routers import SimpleRouter
from .views import DriverViewSet

app_name = 'drivers'

router = SimpleRouter(trailing_slash=False)
router.register(r'drivers', DriverViewSet, basename='drivers')

urlpatterns = router.urls
