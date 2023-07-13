from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # Products: inventory < 10 and price < 20
    query_set = Product.objects.all()[:5]

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
