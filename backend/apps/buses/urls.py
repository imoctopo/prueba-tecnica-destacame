from rest_framework.routers import SimpleRouter
from .views import BusViewSet

app_name = 'buses'

router = SimpleRouter(trailing_slash=False)
router.register(r'buses', BusViewSet, basename='buses')

urlpatterns = router.urls
