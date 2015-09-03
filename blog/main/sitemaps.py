#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap

from . import models

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return models.Post.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.update_time

class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return models.Page.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.update_time

# class CategorySitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6

#     def items(self):
#         return models.Category.objects.all()

# class TagSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6

#     def items(self):
#         return models.Tag.objects.all()

sitemaps = {
    'blog': BlogSitemap,
    'page': PageSitemap,
    # 'category': CategorySitemap,
    # 'tag': TagSitemap,
}

