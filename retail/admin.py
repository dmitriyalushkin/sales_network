from django.contrib import admin
from retail.models import Retail


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('factory',)
    list_filter = ('city_retail',)

