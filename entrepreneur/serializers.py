from rest_framework import serializers
from entrepreneur.models import Entrepreneur


class EntrepreneurSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели предпринимателя """
    class Meta:
        model = Entrepreneur
        fields = '__all__'
