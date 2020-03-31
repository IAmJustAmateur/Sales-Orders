from django.contrib import admin
from sales_orders_app.models import Customer, Order, Sale

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Sale)
