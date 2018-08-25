from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^index/$', views.home),
    url(r'^register/$', views.register),
    url(r'^login/$',views.login_user),
    url(r'^sample/$', views.home3),
    url(r'^logout/$', views.logout),
    url(r'^search/$',views.search),
    url(r'^product/(\d+)$', views.product),
    url(r'^cart/$', views.cart),
    url(r'^checkout/$', views.checkout),
    url(r'^single/$', views.home2),
    url(r'^shop/$', views.shop),
    url(r'^shop/(\w+)$',views.shop2),
    url(r'^delete/(\d+)$',views.delete_cart_item),
    url(r'^shop/$', views.shop),
    url(r'^newarrival/(\d+)$', views.Newarrival),
    url(r'^hacks/$', views.hacks),
    url(r'^mail/$', views.mail2),


]