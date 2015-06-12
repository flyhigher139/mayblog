#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Permission

from guardian.admin import GuardedModelAdmin

from . import models

# Register your models here.

class PostAdmin(GuardedModelAdmin):
    pass

class TagAdmin(GuardedModelAdmin):
    pass

class CategoryAdmin(GuardedModelAdmin):
    pass



admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category)
admin.site.register(models.Page)
admin.site.register(models.BlogMeta)
admin.site.register(Permission)