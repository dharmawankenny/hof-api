# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Award(models.Model):
    rank = models.CharField(max_length=128)
    competition = models.CharField(max_length=256)
    institution = models.CharField(max_length=128)
    participant = models.CharField(max_length=256)
    year = models.IntegerField()

class Member(models.Model):
    role = models.CharField(max_length=128)
    division = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    linkedin = models.CharField(max_length=128)
    photo = models.CharField(max_length=1024, null=True)

# Create your models here.
