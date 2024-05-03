from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

router = DefaultRouter()
router.register('animals', AnimalViewSet)  # Register AnimalViewSet for '/animals/' endpoint

urlpatterns = router.urls
