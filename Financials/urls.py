from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.financial_list, name='financial_list'),
    url(r'^customer/(P<pk>\d+)/$', views.customer_list, name='customer_list'),
    url(r'^crypto/(P<pk>\d+)/$', views.crypto_list, name='crypto_list'),
    url(r'^stock/(P<pk>\d+)/$', views.stock_list, name='stock_list'),
]