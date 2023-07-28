from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage


# @transaction.atomic()
def say_hello(request):
    try:
        # message = EmailMessage('subject', 'message',
        #                        'from@moshbuy.com', ['john@moshbuy.com'])
        # message.attach_file('playground/static/images/munchkin.jpg')
        # message.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={
                'name': 'Mosh'
            }
        )
        message.send(['john@moshbuy.com'])
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
