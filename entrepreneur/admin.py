from django.contrib import admin
from entrepreneur.models import Entrepreneur


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('retail',)
    list_filter = ('city_entrepreneur',)
    actions = ['clear_arrears']

    @admin.action(description='Очищение задолженности перед поставщиком')
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=Entrepreneur.arrears)

