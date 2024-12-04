from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests


logger = logging.getLogger(__name__) # "__name__" will translate to the name of the file, in this case 'playground.views'

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved the response')
            data = response.json()
        except ConnectionError:
            logger.critical('Can not connect to httpbin!')
        return render(request, 'hello.html', {'name': data})
