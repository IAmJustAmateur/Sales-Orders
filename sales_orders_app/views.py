from django.shortcuts import render
from sales_orders_app.models import Customer, Order, Sale
from django.contrib.auth.models import User
from . import forms
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'sales_orders_app/index.html')

@login_required
def special(request):
    return HttpResponse("Yau are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse(index))


def sales(request):
    return render(request, 'sales_orders_app/sales.html')


def orders(request):
    order_list = Order.objects.order_by("customer")
    context = {"orders": order_list}


    return render(request, 'sales_orders_app/orders.html', context)

def customers(request):
    print(" in view.customers")
    customer_list = Customer.objects.order_by('phone')
    if customer_list:
        print(" customer_list is not empty")
    else:
        print("customer_list is empty")
    for customer in customer_list:
        print (customer.phone)
    #print(type(customers_list))
    context = {"customers": customer_list}
    return render(request, 'sales_orders_app/customers.html', context)

def CustomerForm(request):

    registered = False

    print (request.method)
    if request.method =='POST':
        print ("request.method  is POST")
        user_form = forms.CustomerForm(request.POST)
        profile_form = forms.CustomerProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print("both forms are valid")
            print ('============  before saving')

            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            print("========= user saved")

            profile = profile_form.save(commit = False)
            print(" ===   before profile.customer = user")
            profile.user = user
            print(" ===   after profile.user = user")
            print(profile.phone)
            profile.save()
            print("========= profile saved")
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        print("Some other method")
        user_form = forms.CustomerForm()
        print ("user_form created")
        profile_form = forms.CustomerProfileInfoForm()
        print ("profile_form created")
    print ("before return")
    return render(request, 'sales_orders_app/CustomerForm.html', {'customer_form': user_form,
                                                                    'customer_profile_info_form': profile_form,
                                                                    'registered': registered})

def OrderForm(request):
    ordered = False

    if request.method == 'POST':
        print('in POST method')
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save(commit = True)

            ordered = True

        else:
            print ('OrderForm: form is invalid')
    else:
        print('========   Order Form, some other method')
        form = forms.OrderForm()
        print('========== After creating form')
        print(form.Meta.fields)
        print(form.Meta.model)

    print ("=============== before form rendering")

    return render(request, 'sales_orders_app/order_form.html', {'form': form, 'ordered': ordered})

def user_login(request):
    print('in user_login')
    if request.method=='POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        print('in user_login before rendering')
        return render(request, 'sales_orders_app/login.html')
