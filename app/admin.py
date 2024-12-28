from django.contrib import admin
from .models import *

@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )

@admin.register(Goods)
class AdminGoods(admin.ModelAdmin):
    list_display = ('name', 'price', 'decs')
    list_display_links = ('name', 'price', 'decs', )