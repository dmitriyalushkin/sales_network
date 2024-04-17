from django.contrib import admin
from entrepreneur.models import Entrepreneur


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('retail',)
    list_filter = ('city_entrepreneur',)

