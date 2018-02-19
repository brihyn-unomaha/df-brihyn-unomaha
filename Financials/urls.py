from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^stock/(?P<pk>\d+)/$', views.stock_detail, name='stock_detail'),
    url(r'^crypto/(?P<pk>\d+)/$', views.crypto_detail, name='crypto_detail'),
]