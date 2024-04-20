from django.contrib import admin
from factory.models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name_factory',)
    list_filter = ('city_factory',)
    actions = ['clear_arrears']

    @admin.action(description='Очищение задолженности перед поставщиком')
    def clear_arrears(self, request, queryset):
        queryset.update(arreas=Factory.arrears)
