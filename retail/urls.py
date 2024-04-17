from django.urls import path

from retail.apps import RetailConfig
from retail.views import RetailCreateAPIView, RetailListAPIView, \
    RetailRetrieveAPIView, RetailUpdateAPIView, RetailDestroyAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('retail/create/', RetailCreateAPIView.as_view(), name='retail-create'),
    path('retail/', RetailListAPIView.as_view(), name='retail-list'),
    path('retail/<int:pk>/', RetailRetrieveAPIView.as_view(), name='retail-get'),
    path('retail/update/<int:pk>/', RetailUpdateAPIView.as_view(), name='retail-update'),
    path('retail/delete/<int:pk>/', RetailDestroyAPIView.as_view(), name='retail-delete'),
]
