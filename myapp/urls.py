from django.urls import path
from .views import homePageView
from .views import my_django_view

urlpatterns = [
    path('', homePageView, name='home'),
    path('request', my_django_view, name='request')
]