from django.contrib import admin
from .models import Product, Staff, ContactUs, ProductStock

# Register your models here.

admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(ContactUs)
admin.site.register(ProductStock)