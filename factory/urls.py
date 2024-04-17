from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryCreateAPIView, FactoryListAPIView, \
    FactoryRetrieveAPIView, FactoryUpdateAPIView, FactoryDestroyAPIView

app_name = FactoryConfig.name

urlpatterns = [
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/', FactoryListAPIView.as_view(), name='factory-list'),
    path('factory/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory-get'),
    path('factory/update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factory/delete/<int:pk>/', FactoryDestroyAPIView.as_view(), name='factory-delete'),
]
