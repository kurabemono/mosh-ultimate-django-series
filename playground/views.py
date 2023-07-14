from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    # alternate
    # collection = Collection.objects.create(title='a', featured_product_id=1)

    return render(request, 'hello.html', {'name': 'Mosh'})
