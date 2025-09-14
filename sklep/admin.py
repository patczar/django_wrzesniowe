from django.contrib import admin

# Register your models here.
# from sklep.models import Product
from .models import *

admin.site.register(Product)

