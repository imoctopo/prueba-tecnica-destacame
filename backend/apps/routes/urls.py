from rest_framework.routers import SimpleRouter
from .views import RouteViewSet

app_name = 'routes'

router = SimpleRouter(trailing_slash=False)
router.register(r'routes', RouteViewSet, basename='routes')

urlpatterns = router.urls
