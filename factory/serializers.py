from rest_framework import serializers
from factory.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели завода """
    class Meta:
        model = Factory
        fields = '__all__'
