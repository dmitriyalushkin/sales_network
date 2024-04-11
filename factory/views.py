from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from factory.paginators import FactoryPaginator
from factory.permissions import IsModuleOwner, IsLessonOwner

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
    pagination_class = FactoryPaginator
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
    permission_classes = [IsAuthenticated]


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления завода """

    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]
