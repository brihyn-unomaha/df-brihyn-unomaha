from django.db import models
from django.utils import timezone


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    created_date = models.DateTimeField(
            default=timezone.now)
    modified_date = models.DateTimeField(
            blank=True, null=True)

    def addcustomer(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customer_name

class Stock(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    qty = models.IntegerField(null=False, blank=False)
    purchase_price = models.FloatField(null=False, blank=False)
    purchase_date = models.DateTimeField(
            default=timezone.now)
    created_date = models.DateTimeField(
            default=timezone.now)
    modified_date = models.DateTimeField(
            blank=True, null=True)

    def addstock(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.stock_name

class Cryptocurrency(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crypto_name = models.CharField(max_length=100)
    qty = models.IntegerField(null=False, blank=False)
    purchase_price = models.FloatField(null=False, blank=False)
    purchase_date = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
            default=timezone.now)
    modified_date = models.DateTimeField(
            blank=True, null=True)

    def addcrypto(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.crypto_name