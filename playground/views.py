from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        # Sending Email to users:
        # Use send_mass_mail instead of send_mail for sending more than one email
        # send_mail('Subject', 'Message', 'info@miladbuy.com', ['miladvalizadeh2003@gmail.com'])

        # Sending Email to admins:
        # We should configure the admins in the settings.py
        mail_admins('Subject', 'Message', html_message='message')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Milad'})
