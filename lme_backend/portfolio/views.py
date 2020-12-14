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
    # queryset = Transaction.objects.filter(portfolio_id=self.kwargs['portfolio_pk'])
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(portfolio=self.kwargs['portfolio_pk'])

    # def list(self, request, portfolio_pk=None):
    #     queryset = Transaction.objects.filter(portfolio=portfolio_pk)
    #     serializer = TransactionSerializer(queryset, many=True)
    #     print(serializer.data)
        # return Response(serializer.data)

    # def retrieve(self, request, pk=None, portfolio_pk=None):
    #     queryset = Transaction.objects.filter(pk=pk, portfolio=portfolio_pk)
    #     maildrop = get_object_or_404(queryset, pk=pk)
    #     serializer = TransactionSerializer(Transaction)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(pk=self.kwargs['portfolio_pk'])
        serializer.save(portfolio=portfolio)