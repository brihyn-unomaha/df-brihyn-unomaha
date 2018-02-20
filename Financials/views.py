from django.shortcuts import redirect
from django.utils import timezone
from .models import Customer
from .models import Stock
from .models import Cryptocurrency
from .forms import CustomerForm
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

def crypto_list(request):
    cryptocurrency = Cryptocurrency.objects.order_by('crypto_name')
    return render(request, 'Financials/crypto_list.html', {'cryptocurrency':cryptocurrency})

def stock_list(request):
    stock = Stock.objects.order_by('stock_name')
    return render(request, 'Financials/stock_list.html', {'stock':stock})