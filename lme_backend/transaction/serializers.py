from rest_framework import serializers
from .models import Transaction

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
