from rest_framework import generics, permissions
from .models import Bill
from .serializers import BillSerializer, BillCreateSerializer

class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillCreateView(generics.CreateAPIView):
    serializer_class = BillCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)           
