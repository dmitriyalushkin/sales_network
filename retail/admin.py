from django.contrib import admin
from retail.models import Retail


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('factory',)
    list_filter = ('city_retail',)
    actions = ['clear_arrears']

    @admin.action(description='Очищение задолженности перед поставщиком')
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=Retail.arrears)

