# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Workshops(models.Model):
    workshop_name = models.CharField(max_length= 128)
    desc = models.CharField(max_length=524)
    img = models.ImageField(upload_to='images/')

