from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^customer/(?P<pk>\d+)/delete/$', views.customer_delete, name='customer_delete'),
    url(r'^crypto/$', views.crypto_list, name='crypto_list'),
    url(r'^crypto/(?P<pk>\d+)/$', views.crypto_detail, name='crypto_detail'),
    url(r'^crypto/new/$', views.crypto_new, name='crypto_new'),
    url(r'^crypto/(?P<pk>\d+)/edit/$', views.crypto_edit, name='crypto_edit'),
    url(r'^crypto/(?P<pk>\d+)/delete/$', views.crypto_delete, name='crypto_delete'),
    url(r'^stock/$', views.stock_list, name='stock_list'),
    url(r'^stock/(?P<pk>\d+)/$', views.stock_detail, name='stock_detail'),
    url(r'^stock/new/$', views.stock_new, name='stock_new'),
    url(r'^stock/(?P<pk>\d+)/edit/$', views.stock_edit, name='stock_edit'),
    url(r'^stock/(?P<pk>\d+)/delete/$', views.stock_delete, name='stock_delete'),
]