from django.shortcuts import render
import requests


def say_hello(request):
    # Simulating a slow third party service that takes 2 seconds to respond
    requests.get('https://httpbin.org/delay/2')
    return render(request, 'hello.html', {'name': 'Milad'})
