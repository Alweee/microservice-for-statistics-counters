from rest_framework import serializers

from api.models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Statistics
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm',)

    def get_cpc(self, obj): # проблема, данные тут не считаются на ходу.
        if obj.cost or obj.clicks is None:
            return
        return obj.cost / obj.clicks

    def get_cpm(self, obj):
        if obj.cost or obj.views is None:
            return
        return (obj.cost/obj.views) * 1000
