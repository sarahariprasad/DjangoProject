from django.shortcuts import render, redirect

# Create your views here.
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View






class Login(View):
    def get(self, request):

          return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')

        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        name = Customer.get_customer_details()


        error_message = None

        if customer:
            flag = check_password(password, customer.password)

            if flag:

                request.session['customer'] = customer.id
                return redirect('homepage')
            else:
                error_message = 'Password Invalid !!'
        else:
            error_message = 'Email  Invalid !!'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def profile(self,request):
    customers = request.session.get('customer')

    if customers:
        for cust in customers:
            name = cust.first_name
            email = cust.email
            context = {
                'name':name,
                'email':email
            }
        return render(request, 'base.html',context)
    else:
        return False


def logout(request):
    request.session.clear()
    return redirect('/')

