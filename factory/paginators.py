from rest_framework.pagination import PageNumberPagination


class FactoryPagination(PageNumberPagination):
    page_size = 1
