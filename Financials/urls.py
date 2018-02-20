from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
]