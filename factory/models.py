from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    '''Модель завода'''

    name_factory = models.CharField(max_length=50, verbose_name='название завода')
    email_factory = models.EmailField(max_length=50, verbose_name='почта завода')
    country_factory = models.CharField(max_length=50, verbose_name='страна завода')
    city_factory = models.CharField(max_length=50, verbose_name='город завода')
    street_factory = models.CharField(max_length=50, verbose_name='улица завода')
    house_number_factory = models.IntegerField(default=0, verbose_name='номер дома завода')

    name_product = models.CharField(max_length=50, verbose_name='название продукта')
    model_product = models.CharField(max_length=50, verbose_name='модель продукта')
    date_product_release = models.DateField(default=date.today,
                                            verbose_name='дата выхода продукта на рынок')

    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность')
    time_create = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name_factory}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'
