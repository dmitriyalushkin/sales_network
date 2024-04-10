from django.db import models
from datetime import date
from django.utils import timezone

from factory.models import Factory

NULLABLE = {'blank': True, 'null': True}


class Retail(models.Model):
    '''Модель розничной сети'''

    name_retail = models.CharField(max_length=50, verbose_name='название розничной сети')
    email_retail = models.EmailField(max_length=50, verbose_name='почта розничной сети')
    country_retail = models.CharField(max_length=50, verbose_name='страна розничной сети')
    city_retail = models.CharField(max_length=50, verbose_name='город розничной сети')
    street_retail = models.CharField(max_length=50, verbose_name='улица розничной сети')
    house_number_retail = models.IntegerField(default=0, verbose_name='номер дома розничной сети')

    name_product = models.CharField(max_length=50, verbose_name='название продукта')
    model_product = models.CharField(max_length=50, verbose_name='модель продукта')
    date_product_release = models.DateField(default=date.today,
                                            verbose_name='дата выхода продукта на рынок')

    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='завод')
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность')
    time_create = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    def __str__(self):
        return f'{self.name_retail}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'
