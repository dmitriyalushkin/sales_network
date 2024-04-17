from django.urls import path

from entrepreneur.apps import EntrepreneurConfig
from entrepreneur.views import EntrepreneurCreateAPIView, EntrepreneurListAPIView, \
    EntrepreneurRetrieveAPIView, EntrepreneurUpdateAPIView, EntrepreneurDestroyAPIView

app_name = EntrepreneurConfig.name

urlpatterns = [
    path('entrepreneur/create/', EntrepreneurCreateAPIView.as_view(), name='entrepreneur-create'),
    path('entrepreneur/', EntrepreneurListAPIView.as_view(), name='entrepreneur-list'),
    path('entrepreneur/<int:pk>/', EntrepreneurRetrieveAPIView.as_view(), name='entrepreneur-get'),
    path('entrepreneur/update/<int:pk>/', EntrepreneurUpdateAPIView.as_view(), name='entrepreneur-update'),
    path('entrepreneur/delete/<int:pk>/', EntrepreneurDestroyAPIView.as_view(), name='entrepreneur-delete'),
]
