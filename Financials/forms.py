from django import forms

from .models import Customer
from .models import Cryptocurrency
from .models import Stock

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('customer_name','street_address','city','state','zip','email','phone',)

class CryptoForm(forms.ModelForm):

    class Meta:
        model = Cryptocurrency
        fields = ('crypto_name','customer','qty','purchase_price','purchase_date',)

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_name','customer','symbol','qty','purchase_price','purchase_date',)