from django.contrib import admin

from dore.models.categories import Category
from dore.models.products import Product

#from .models import *

# Register your models here


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']


admin.site.register(Product)
admin.site.register(Category)
