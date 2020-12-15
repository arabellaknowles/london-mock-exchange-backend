from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .serializers import PortfolioSerializer, TransactionSerializer
from .models import Portfolio, Transaction 

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        user = Token.objects.get(key=self.request.headers.Authorization).user
        # print('self', self)
        # print('self.request', self.request)
        # print('self.request.headers', self.request.headers)
        # print('self.request.headers.authorization', self.request.headers.Authorization)
        return Portfolio.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        user = Token.objects.get(key=self.request.headers.Authorization).user
        print(user)
        serializer.save(owner=user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(portfolio=self.kwargs['portfolio_pk'])

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(pk=self.kwargs['portfolio_pk'])
        serializer.save(portfolio=portfolio)