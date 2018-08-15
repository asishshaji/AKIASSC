# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . import models
from .forms import EnquiryForm
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    workshops = models.Workshops.objects.all()
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('test')
    else:
        form = EnquiryForm()

    email = EmailMessage('Subject', 'Body', to=['mrkai1253@gmail.com'])
    email.send()
    context = {
        'workshops': workshops,
        'enquiry_form': form
    }

    return render(request, 'akiassc.html', context)
