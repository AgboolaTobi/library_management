from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def greet(request):
    subject = "Hi user"
    message = "this mail was sent using django"
    email_message = EmailMessage(subject=subject, body=message, from_email='info@librarian.com',to=['toby@librarian.com'])
    email_message.attach_file('')
    email_message.send()
    send_mail(subject, message,
              'info@librarian.com',
              ['toby@librarian.com'])
    return render(request, 'demo/hello.html')


def greet_name(request, name):
    return HttpResponse(f"Welcome {name}! Let's xpore django...")
