from django.shortcuts import render
from django.db import connection
from store.models import Collection, Order, OrderItem, Product
from tags.models import TaggedItem


# @transaction.atomic()
def say_hello(request):

    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(query_set)})
