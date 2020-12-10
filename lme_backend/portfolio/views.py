from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PortfolioSerializer
from .models import Portfolio

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('name')
    serializer_class = PortfolioSerializer