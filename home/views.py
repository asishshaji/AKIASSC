# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    workshops = models.Workshops.objects.all()

    context = {
        'workshops': workshops
    }

    return render(request, 'akiassc.html', context)
