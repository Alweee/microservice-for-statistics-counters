from rest_framework import filters
from django_filters import DateRangeFilter, DateFilter # может быть поможет эта библиотека в моём таске, разобраться.

from api.mixins import CreateRetrieveDestroyViewSet
from api.models import Statistics
from api.serializers import StatisticsSerializer


class StatisticsViewSet(CreateRetrieveDestroyViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    # filterset_class такая штука ещё есть
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
