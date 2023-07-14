from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection(pk=11)
    collection.delete()

    Collection.objects.filter(pk__gt=5).delete()

    return render(request, 'hello.html', {'name': 'Mosh'})
