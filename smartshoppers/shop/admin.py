from django.contrib import admin
from .models import StoreCategory, Store, Coupon

admin.site.register(StoreCategory)
admin.site.register(Store)
admin.site.register(Coupon)