from django.db import models


class Statistics(models.Model):
    date = models.DateTimeField(
        verbose_name='дата события',
        auto_now_add=True,
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
