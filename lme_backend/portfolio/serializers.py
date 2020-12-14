from rest_framework import serializers
from .models import Portfolio, Transaction

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name', 'net_earnings', 'owner_id')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = (
          'ticker',
          'instrument_name',
          'number_of_shares',
          'trade_date',
          'close_out_date',
          'buy_price',
          'sell_price',
          'net_earnings',
          'portfolio_id'
          )
