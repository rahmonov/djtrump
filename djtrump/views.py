import requests

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    res = requests.get('{base_url}{endpoint}'.format(base_url=settings.BASE_API_URL, endpoint='/quotes/random'))

    if not res.ok:
        return HttpResponse('Something went wrong. Please, try again later.')

    return render(request, 'djtrump/index.html', {'data': res.json()})


def personalize(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            name = 'Stupid User'

        res = requests.get('{base_url}{endpoint}'.format(
            base_url=settings.BASE_API_URL, endpoint='/quotes/personalized?q='+name)
        )

        if not res.ok:
            return HttpResponse('Something went wrong. Please, try again later.')

        return render(request, 'djtrump/index.html', {'data': res.json(), 'name': name})
