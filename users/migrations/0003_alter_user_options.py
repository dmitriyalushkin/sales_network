# Generated by Django 5.0.4 on 2024-04-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
