from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


# @transaction.atomic()
def say_hello(request):
    try:
        # send_mail('subject', 'message',
        #           'info@moshbuy.com', ['bob@moshbuy.com'])
        mail_admins('subject', 'message', html_message='message')
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
