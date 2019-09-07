from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ListSerializer, CardSerializer
from .models import List, Card


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()  # From where it takes data
    serializer_class = ListSerializer  # Specifies what fields are converted to JSON
    permission_classes = (permissions.IsAuthenticated,)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)

# View classes
# View is a component that takes request and retrieve data and convert it to JSON
# We want our data to be visible only for logged in users
# permission_classes has to be a tuple (if 1 item, finish with comma)

# Cross-site request forgery (CSRF) protection
# How to configure Angular to handle Django CSRF cookie?
# New script, in which we retrieve angular module and call run() with a function as argument
# List argument - function (last item) with its dependencies
# Custom function run depends on htttp service
# Executed at the start of application, after loaded modules
# Set two options on http service: name of CSRF token cookie (Django sets)
# and name of the header that Angular should sent with its AJAX request

# Login has to be protected always
# Use decorators for Django views: csrf_protect - (login view has to be always protected)
# and ensure_csrf_cookie - force Django to always set CSRF cookie for a view
# On server it will has to be HTTPS (to not expose user credentials)

# TODO: Uncouple front-end from Django Apps
# In Django front-end inside app folder, but it does not fit this situation
