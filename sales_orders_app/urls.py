from django.urls import path
from . import views

app_name = 'sales_orders_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('sales/', views.sales, name='sales'),
    path('orders/', views.orders, name='orders'),
    path('CustomerForm/', views.CustomerForm, name='CustomerForm'),
    path('customers/', views.customers, name='customers'),
    path('OrderForm/', views.OrderForm, name = 'OrderForm'),
    path('login/', views.user_login, name= 'user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special')
]
