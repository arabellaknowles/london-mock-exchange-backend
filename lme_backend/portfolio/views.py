from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .serializers import PortfolioSerializer, TransactionSerializer
from .models import Portfolio, Transaction 

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        user = Token.objects.get(key=self.request.headers['Authorization']).user
        return Portfolio.objects.filter(owner=user)

    def perform_create(self, serializer):
        user = Token.objects.get(key=self.request.headers['Authorization']).user
        serializer.save(owner=user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(portfolio=self.kwargs['portfolio_pk'])

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(pk=self.kwargs['portfolio_pk'])
        portfolio.calculate_net_profit()
        print('im in perform create')
        serializer.save(portfolio=portfolio)