from rest_framework import filters
from django_filters import rest_framework as rest_filters

from api.mixins import CreateRetrieveDestroyViewSet
from api.models import Statistics
from api.serializers import StatisticsSerializer


class DateFilter(rest_filters.FilterSet):
    date = rest_filters.DateFromToRangeFilter()

    class Meta:
        model = Statistics
        fields = ('date',)


class StatisticsViewSet(CreateRetrieveDestroyViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    filterset_class = DateFilter
    filter_backends = (filters.OrderingFilter,
                       rest_filters.DjangoFilterBackend,)
    ordering_fields = '__all__'
    ordering = ('date',)
