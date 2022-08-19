from django.contrib import admin
from .models import Product, Order, Students, Placements, Companies


# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Students)
admin.site.register(Placements)
admin.site.register(Companies)