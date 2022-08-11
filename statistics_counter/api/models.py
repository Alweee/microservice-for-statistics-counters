from django.db import models


class Statistics(models.Model):
    """Класс счётчиков статистики."""
    date = models.DateField(
        verbose_name='дата события',
    )
    views = models.IntegerField(
        verbose_name='количество показов',
        blank=True,
        null=True,
    )
    clicks = models.IntegerField(
        verbose_name='количество кликов',
        blank=True,
        null=True,
    )
    cost = models.FloatField(
        verbose_name='стоимость кликов',
        blank=True,
        null=True,
    )

    @property  # попробовать решить проблему вычисления данных на лету вот так.
    def get_cpc(self):
        pass
