from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('Subject', 'Message', 'from@miladbuy.com', ['john@miladbuy.com'])
        message.attach_file('playground/static/images/dog.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Milad'})
