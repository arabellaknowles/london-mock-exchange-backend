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
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(portfolio=self.kwargs['portfolio_pk'])

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(pk=self.kwargs['portfolio_pk'])
        serializer.save(portfolio=portfolio)