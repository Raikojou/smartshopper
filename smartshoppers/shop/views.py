from django.shortcuts import render, get_object_or_404
from .models import Coupon, Store, StoreCategory

def homepage(request):

    context = {
        'all_stores': Store.objects.all(),
    }
    return render(request, 'shop/home.html', context)

def store(request, slug):
    store = get_object_or_404(Store, slug=slug)
    return render(request, 'shop/shop_page.html', {'store': store})