from datetime import datetime

from rest_framework import serializers
from django.forms import ValidationError

from api.models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Statistics
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm',)

    def get_cpc(self, obj):
        if (obj.cost and obj.clicks) is None:
            return 0
        return round(obj.cost / obj.clicks, 2)

    def get_cpm(self, obj):
        if (obj.cost and obj.views) is None:
            return 0
        return round((obj.cost/obj.views) * 1000, 2)

    def validate_date(self, value):
        if str(value) > str(datetime.today().strftime('%Y-%m-%d')):
            raise ValidationError('Дата не может быть больше текущей')
        return value
