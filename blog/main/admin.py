#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Permission

from guardian.admin import GuardedModelAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

from . import models




class PostResource(resources.ModelResource):

    class Meta:
        model = models.Post

class TagResource(resources.ModelResource):

    class Meta:
        model = models.Tag

class CategoryResource(resources.ModelResource):

    class Meta:
        model = models.Category

class PageResource(resources.ModelResource):

    class Meta:
        model = models.Page

class BlogMetaResource(resources.ModelResource):

    class Meta:
        model = models.BlogMeta

class PermissionResource(resources.ModelResource):

    class Meta:
        model = Permission


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class PageAdmin(ImportExportModelAdmin):
    resource_class = PageResource

class BlogMetaAdmin(ImportExportModelAdmin):
    resource_class = BlogMetaResource

class PermissionAdmin(ImportExportModelAdmin):
    resource_class = Permission



admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.BlogMeta, BlogMetaAdmin)
admin.site.register(Permission, PermissionAdmin)