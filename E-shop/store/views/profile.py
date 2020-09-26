from django.shortcuts import render
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class Profile(View):
    def get(self,request):
        customer1 = request.session.get('customer')
        customer = Customer.objects.all(customer1)
        print(customer)

        return render(request, 'base.html',{'customer':customer})









