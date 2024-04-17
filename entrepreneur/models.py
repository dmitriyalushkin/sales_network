from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone

from retail.models import Retail

NULLABLE = {'blank': True, 'null': True}


class Entrepreneur(models.Model):
    '''Модель предпринимателя'''

    name_entrepreneur = models.CharField(max_length=50, verbose_name='имя предпринимателя')
    email_entrepreneur = models.EmailField(max_length=50, verbose_name='почта предпринимателя')
    country_entrepreneur = models.CharField(max_length=50, verbose_name='страна предпринимателя')
    city_entrepreneur = models.CharField(max_length=50, verbose_name='город предпринимателя')
    street_entrepreneur = models.CharField(max_length=50, verbose_name='улица предпринимателя')
    house_number_entrepreneur = models.IntegerField(default=0, verbose_name='номер дома предпринимателя')

    name_product = models.CharField(max_length=50, verbose_name='название продукта')
    model_product = models.CharField(max_length=50, verbose_name='модель продукта')
    date_product_release = models.DateField(default=date.today,
                                            verbose_name='дата выхода продукта на рынок')

    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, verbose_name='розничная сеть')
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность')
    time_create = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name_entrepreneur}'

    class Meta:
        verbose_name = 'предприниматель'
        verbose_name_plural = 'предприниматели'
