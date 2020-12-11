from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PortfolioSerializer
from .models import Portfolio

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)