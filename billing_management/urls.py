from django.urls import path
from .views import BillListView, BillCreateView

urlpatterns = [
    path('bills/', BillListView.as_view(), name='bill-list'),
    path('bill-create/', BillCreateView.as_view(), name='bill-create')
]