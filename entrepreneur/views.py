from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from entrepreneur.permissions import IsUserOrActive, CustomUpdatePermission

from entrepreneur.paginators import EntrepreneurPagination

from entrepreneur.models import Entrepreneur
from entrepreneur.serializers import EntrepreneurSerializer


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """ Класс создания предпринимателя """

    serializer_class = EntrepreneurSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_entrepreneur = serializer.save()
        new_entrepreneur.user = self.request.user
        new_entrepreneur.save()


class EntrepreneurListAPIView(generics.ListAPIView):
    """ Класс просмотра списка предпринимателей """

    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = EntrepreneurPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ('country_entrepreneur',)


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра предпринимателя """

    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated]


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения предпринимателя """

    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated | IsUserOrActive | CustomUpdatePermission]


class EntrepreneurDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления предпринимателя """

    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated | IsUserOrActive]
