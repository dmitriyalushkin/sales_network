from rest_framework import serializers
from retail.models import Retail


class RetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели розничной сети """
    class Meta:
        model = Retail
        fields = '__all__'
