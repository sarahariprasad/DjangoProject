from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Profile(models.Model):
    first_name = models.CharField(max_length=50, default='')
    email = models.EmailField()

    def customerProfile(self):
        return self.save()



    @staticmethod
    def get_customers_by_first_name(first_name):
        return Customer .objects .filter(first_name=first_name)


