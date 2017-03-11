import requests

from django.conf import settings
from django.http import HttpResponse


def index(request):
    res = requests.get('{base_url}{endpoint}'.format(base_url=settings.BASE_API_URL, endpoint='/quotes/random'))

    if not res.ok:
        return HttpResponse('Something went wrong. Please, try again later.')

    return HttpResponse('Trump says: {message}'.format(message=res.json()['message']))
