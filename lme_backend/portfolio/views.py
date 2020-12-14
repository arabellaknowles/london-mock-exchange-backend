from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PortfolioSerializer, TransactionSerializer
from .models import Portfolio, Transaction 

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save()