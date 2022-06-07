from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import logging
logger = logging.getLogger('app_api')

def homePageView(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    template = loader.get_template('base.html')
    r = requests.get('https://ipinfo.io/json', params=request.GET)
    if r.status_code == 200:
        json = r.json()
    else:
        json = { ip : '?' }
    context = { 'ip': json, 'clientip': ip }
    return HttpResponse(template.render(context, request))


def my_django_view(request):
    r = requests.get('https://ipinfo.io/json', params=request.GET)
    if r.status_code == 200:
        return HttpResponse(r)
    return HttpResponse('Could not save data')




