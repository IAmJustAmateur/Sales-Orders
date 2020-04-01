from django.db import models
#from phone_field import PhoneField
from django.utils import timezone
from django.contrib.auth.models import User

sizes_list = ['42', '44', '46', '48', '50', '52']

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True,)
    #first_name = models.CharField(max_length = 30)
    #phone = PhoneField(blank=True, help_text='номер телефона')
    phone =  models.CharField(max_length = 20)
    portfolio_site = models.URLField(blank = True)
    #email = models.EmailField(max_length=100)
    info = models.CharField(max_length = 255)
    #picture = models.ImageField(upload_to = 'profile_pic', blank=True)

    def __str__(self):
        #return "{}, телефон: {}".format(self.first_name, self.phone)
        return "{}, телефон: {}".format(self.user.username, self.phone)

class Order(models.Model):
    print('Creating Order Form')
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    vendor_code = models.CharField(max_length = 6)
    # select color from list
    color = models.CharField(max_length = 20)
    # select size from list
    size = models.CharField(max_length=2) # choices = sizes_list
    current_date = models.DateField(default=timezone.now)
    executed = models.BooleanField(default = False)


    def __str__(self):
        if self.executed:
            executed = 'выполнено'
        else:
            executed = 'не выполнено'
        return "дата: {}, артикул: {}, цвет: {}, размер {}, {}, {}".format(self.current_date, self.vendor_code, self.color,
                                                                self.size, self.customer, executed)

class Sale(models.Model):
    vendor_code: models.CharField(max_length = 6)
    color = models.CharField(max_length = 20)
    size = models.CharField(max_length=2) # choices = sizes_list
    price = models.FloatField()
    date = models.DateField()

    # optional Customer ???

    def __str__(self):
        return "дата: {}, артикул: {}, цена: {}, цвет {}, размер {}".format(self.date,
                                                                    self.vendor_code,
                                                                    self.price,
                                                                    self.color, self.size)
