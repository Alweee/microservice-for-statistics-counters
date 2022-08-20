from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import StatisticsViewSet

router_v1 = DefaultRouter()
router_v1.register('statistics', StatisticsViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls), name='statistics'),
]
