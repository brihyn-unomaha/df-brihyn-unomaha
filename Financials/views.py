from django.shortcuts import render

# Create your views here.

def financial_list(request):
    return render(request, 'Financials/financial_list.html', {})

def customer_list(request):
    return render(request, 'Financials/customer_list.html', {})

def crypto_list(request):
    return render(request, 'Financials/crypto_list.html', {})

def stock_list(request):
    return render(request, 'Financials/stock_list.html', {})