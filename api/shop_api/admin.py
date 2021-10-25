from django.contrib import admin
from .models import *

# class ProductAdmin(admin.ModelAdmin):
#     fields = ('category', 'company', 'title', 'slug', 'short_desc', 'desc', 'basic_price')

admin.site.register(Product)
admin.site.register(Switch)
admin.site.register(KeyboardSwitches)
admin.site.register(Characteristic)
admin.site.register(ProductCharacteristic)
admin.site.register(Photos)
admin.site.register(Company)
admin.site.register(Category)
