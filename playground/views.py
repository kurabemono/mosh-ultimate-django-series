from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError


# @transaction.atomic()
def say_hello(request):
    try:
        message = EmailMessage('subject', 'message',
                               'from@moshbuy.com', ['john@moshbuy.com'])
        message.attach_file('playground/static/images/munchkin.jpg')
        message.send()
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
