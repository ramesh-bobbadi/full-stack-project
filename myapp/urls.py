from django.urls import path
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country',CountryViewset,basename='country')
router.register('league',LeagueViewset,basename='league')
router.register('characteristic',CharacteristicViewset,basename='characterristic')

urlpatterns = router.urls