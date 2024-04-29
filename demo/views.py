from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def greet(request):
    subject = "Hi user"
    message = "this mail was sent using django"
    send_mail(subject, message,
              'info@librarian.com',
              ['toby@librarian.com'])
    return render(request, 'demo/hello.html')


def greet_name(request, name):
    return HttpResponse(f"Welcome {name}! Let's xpore django...")
