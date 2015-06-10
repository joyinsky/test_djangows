#!/usr/bin/env python
from django.conf.urls import patterns, url
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from .views import AvayaService
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^avaya/$', csrf_exempt(DjangoView.as_view(services=[AvayaService], tns='mango.avaya.service',
                                        in_protocol=Soap11(), out_protocol=Soap11()))),
]