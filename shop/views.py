from django.shortcuts import render, get_object_or_404
from .models import Coupon, Store, StoreCategory
from django.db.models import Q

def homepage(request):

    context = {
        'all_stores': Store.objects.all(),
    }
    return render(request, 'shop/home.html', context)

def store(request, slug):
    store = get_object_or_404(Store, slug=slug)
    return render(request, 'shop/shop_page.html', {'store': store})

def store_search(request):
    query = request.GET.get('query', '')
    results = []
    more_results = False

    if query:
        all_results = Store.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()
        more_results = all_results.count() > 5
        results = all_results[:5]
    
    context = {
        'results': results,
        'more_results': more_results,
        'query': query
    }

    return render(request, 'shop/partial/store_search.html', context)

def full_store_search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Store.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()

    context = {
        'results': results,
        'query': query
    }

    return render(request, 'shop/full_store_search.html', context)