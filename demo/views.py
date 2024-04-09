from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def greet(request):
    return render(request, 'demo/hello.html', {'name': "Toby"})


def greet_name(request, name):
    return HttpResponse(f"Welcome {name}! Let's xpore django...")
