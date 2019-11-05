from rest_framework import routers
from .api import LeadViewSet  # from api file then the class name

router = routers.DefaultRouter()

router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
