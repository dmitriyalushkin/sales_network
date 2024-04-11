from django.contrib import admin
from factory.models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = '__all__'
