from django.contrib import admin
from factory.models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name_factory',)
    list_filter = ('city_factory',)
