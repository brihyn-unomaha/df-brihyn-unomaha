from django.shortcuts import redirect
from django.utils import timezone
from .models import Customer
from .models import Stock
from .models import Cryptocurrency
from .forms import CustomerForm
from .forms import CryptoForm
from .forms import StockForm
from django.shortcuts import render, get_object_or_404


# Create your views here.

def customer_list(request):
    customers = Customer.objects.order_by('customer_name')
    return render(request, 'Financials/customer_list.html', {'customers':customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'Financials/customer_detail.html', {'customer': customer})

def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            customer.published_date = timezone.now()
            customer.modified_date = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'Financials/customer_edit.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            customer.published_date = timezone.now()
            customer.modified_date = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'Financials/customer_edit.html', {'form': form})

def customer_delete(request,pk):
    instance = Customer.objects.get(pk=pk)
    instance.delete()
    customers = Customer.objects.order_by('customer_name')
    return render(request, 'Financials/customer_list.html', {'customers': customers})

def crypto_list(request):
    cryptocurrency = Cryptocurrency.objects.order_by('crypto_name')
    return render(request, 'Financials/crypto_list.html', {'cryptocurrency':cryptocurrency})

def crypto_detail(request, pk):
    crypto = get_object_or_404(Cryptocurrency, pk=pk)
    return render(request, 'Financials/crypto_detail.html', {'crypto': crypto})

def crypto_new(request):
    if request.method == "POST":
        form = CryptoForm(request.POST)
        if form.is_valid():
            crypto = form.save(commit=False)
            crypto.author = request.user
            crypto.purchase_date = timezone.now()
            crypto.published_date = timezone.now()
            crypto.modified_date = timezone.now()
            crypto.save()
            return redirect('crypto_detail', pk=crypto.pk)
    else:
        form = CryptoForm()
    return render(request, 'Financials/crypto_edit.html', {'form': form})

def crypto_edit(request, pk):
    crypto = get_object_or_404(Cryptocurrency, pk=pk)
    if request.method == "POST":
        form = CryptoForm(request.POST, instance=crypto)
        if form.is_valid():
            crypto = form.save(commit=False)
            crypto.author = request.user
            crypto.published_date = timezone.now()
            crypto.modified_date = timezone.now()
            crypto.save()
            return redirect('customer_detail', pk=crypto.pk)
    else:
        form = CryptoForm(instance=crypto)
    return render(request, 'Financials/crypto_edit.html', {'form': form})

def crypto_delete(request,pk):
    instance = Cryptocurrency.objects.get(pk=pk)
    instance.delete()
    crypto = Cryptocurrency.objects.order_by('crypto_name')
    return render(request, 'Financials/crypto_list.html', {'crypto': crypto})

def stock_list(request):
    stock = Stock.objects.order_by('stock_name')
    return render(request, 'Financials/stock_list.html', {'stock':stock})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'Financials/stock_detail.html', {'stock': stock})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.author = request.user
            stock.purchase_date = timezone.now()
            stock.published_date = timezone.now()
            stock.modified_date = timezone.now()
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm()
    return render(request, 'Financials/stock_edit.html', {'form': form})

def stock_edit(request, pk):
    stock = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.author = request.user
            stock.published_date = timezone.now()
            stock.modified_date = timezone.now()
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'Financials/stock_edit.html', {'form': form})

def stock_delete(request,pk):
    instance = Stock.objects.get(pk=pk)
    instance.delete()
    stock = Stock.objects.order_by('stock_name')
    return render(request, 'Financials/stock_list.html', {'stock': stock})