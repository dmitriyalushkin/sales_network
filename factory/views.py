from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from factory.permissions import IsUserOrActive, CustomUpdatePermission

from factory.paginators import FactoryPagination

from factory.models import Factory
from factory.serializers import FactorySerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    """ Класс создания завода """

    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_factory = serializer.save()
        new_factory.user = self.request.user
        new_factory.save()


class FactoryListAPIView(generics.ListAPIView):
    """ Класс просмотра списка заводов """

    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = FactoryPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ('country_factory',)


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра завода """

    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения завода """

    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated | IsUserOrActive | CustomUpdatePermission]


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления завода """

    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated | IsUserOrActive]
