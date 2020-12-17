from django.db import models
from users.models import CustomUser

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=60)
    net_earnings = models.FloatField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
           return self.name

    def calculate_net_profit():
        print("im in the calcualate method")
        net_profit = 0
        transactions =  Transaction.objects.filter(portfolio=self.id)
        print('transactions', transactions)
        for transaction in transactions:
            net_profit += transaction['net_earnings']
        print('in the calculate net profit method')
        print('net_profit', net_profit)
        Portfolio.objects.get(id=self.id).update(net_earnings=net_profit)

class Transaction(models.Model):
    ticker = models.CharField(max_length=60)
    instrument_name = models.CharField(max_length=60)
    number_of_shares = models.IntegerField()
    trade_date = models.DateField()
    close_out_date = models.DateField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    net_earnings = models.FloatField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker
