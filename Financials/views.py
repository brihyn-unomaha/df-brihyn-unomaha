from django.shortcuts import render
from .models import Customer
from .models import Stock
from .models import Cryptocurrency
from django.shortcuts import render, get_object_or_404

# Create your views here.

def customer_list(request):
    customers = Customer.objects.order_by('customer_name')
    return render(request, 'Financials/customer_list.html', {'customers':customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'Financials/customer_detail.html', {'customer': customer})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'Financials/stock_detail.html', {'stock': stock})

def crypto_detail(request, pk):
    cryptocurrency = get_object_or_404(Cryptocurrency, pk=pk)
    return render(request, 'Financials/cryptocurrency_detail.html', {'cryptocurrency': cryptocurrency})
