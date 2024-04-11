from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from retail.paginators import RetailPaginator
from retail.permissions import IsModuleOwner, IsLessonOwner

from retail.models import Retail
from retail.serializers import RetailSerializer


class RetailCreateAPIView(generics.CreateAPIView):
    """ Класс создания розничной сети """

    serializer_class = RetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_retail = serializer.save()
        new_retail.user = self.request.user
        new_retail.save()


class RetailListAPIView(generics.ListAPIView):
    """ Класс просмотра списка розничных сетей """

    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = RetailPaginator
    filter_backends = [OrderingFilter]
    ordering_fields = ('country_factory',)


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра розничной сети """

    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]


class RetailUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения розничной сети """

    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]


class RetailDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления розничной сети """

    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]
