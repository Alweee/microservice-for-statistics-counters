from api.mixins import CreateRetrieveDestroyViewSet
from api.models import Statistics
from api.serializers import StatisticsSerializer


class StatisticsViewSet(CreateRetrieveDestroyViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
