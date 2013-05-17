from django.db import models
from django.utils.translation import ugettext_lazy


class SubProduct(models.Model):
    prices = models.ManyToManyField('Price', verbose_name=ugettext_lazy('Prices of Product'))

    class Meta:
        app_label = 'price_monitor'
        verbose_name = ugettext_lazy('SubProduct')
        verbose_name_plural = ugettext_lazy('SubProducts')
