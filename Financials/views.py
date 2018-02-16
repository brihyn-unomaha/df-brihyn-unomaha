from django.shortcuts import render
from .models import Customer
from .models import Stock
from .models import Cryptocurrency

# Create your views here.

def customer_list(request):
    customers = Customer.objects.order_by('customer_name')
    return render(request, 'Financials/customer_list.html', {'customers':customers})

def crypto_list(request):
    crypto = Cryptocurrency.objects.order_by('crypto_name')
    return render(request, 'Financials/crypto_list.html', {'crypto':crypto})

def stock_list(request):
    stocks = Stock.objects.order_by('stock_name')
    return render(request, 'Financials/stock_list.html', {'stocks':stocks})