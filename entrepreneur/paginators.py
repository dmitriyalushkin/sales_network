from rest_framework.pagination import PageNumberPagination


class EntrepreneurPagination(PageNumberPagination):
    page_size = 1
