# Generated by Django 5.0.4 on 2024-04-10 18:31

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_factory', models.CharField(max_length=50, verbose_name='название завода')),
                ('email_factory', models.EmailField(max_length=50, verbose_name='почта завода')),
                ('country_factory', models.CharField(max_length=50, verbose_name='страна завода')),
                ('city_factory', models.CharField(max_length=50, verbose_name='город завода')),
                ('street_factory', models.CharField(max_length=50, verbose_name='улица завода')),
                ('house_number_factory', models.IntegerField(default=0, verbose_name='номер дома завода')),
                ('name_product', models.CharField(max_length=50, verbose_name='название продукта')),
                ('model_product', models.CharField(max_length=50, verbose_name='модель продукта')),
                ('date_product_release', models.DateField(default=datetime.date.today, verbose_name='дата выхода продукта на рынок')),
                ('arrears', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания')),
            ],
            options={
                'verbose_name': 'завод',
                'verbose_name_plural': 'заводы',
            },
        ),
    ]
