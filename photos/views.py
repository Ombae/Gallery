# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image,Location
# Create your views here.

def index(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'home.html',{"images":images, "location": location})
