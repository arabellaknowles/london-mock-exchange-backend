from django.db import models
from users.models import CustomUser

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=60)
    net_earnings = models.FloatField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
           return self.name

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
