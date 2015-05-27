#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Permission
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.Catagory)
admin.site.register(models.BlogMeta)
admin.site.register(Permission)