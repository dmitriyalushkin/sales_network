from rest_framework.pagination import PageNumberPagination


class RetailPagination(PageNumberPagination):
    page_size = 1
