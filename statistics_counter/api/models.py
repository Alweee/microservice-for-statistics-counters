from django.db import models

from api.validators import validate_value


class Statistics(models.Model):
    """Класс счётчиков статистики."""
    date = models.DateField(
        verbose_name='дата события',
    )
    views = models.IntegerField(
        verbose_name='количество показов',
        blank=True,
        null=True,
        validators=(validate_value,),
    )
    clicks = models.IntegerField(
        verbose_name='количество кликов',
        blank=True,
        null=True,
        validators=(validate_value,),
    )
    cost = models.FloatField(
        verbose_name='стоимость кликов',
        blank=True,
        null=True,
        validators=(validate_value,),
    )
