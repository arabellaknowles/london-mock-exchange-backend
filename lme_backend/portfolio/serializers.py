from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name', 'balance', 'net_earnings', 'owner_id')