#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
import markdown2

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=256, default='new blog')
    abstract = models.TextField(null=True, blank=True)
    raw = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content_html = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey('Category', null=True, blank=True)
    is_draft = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.content_html = markdown2.markdown(self.raw, extras=['code-friendly', 'fenced-code-blocks']).encode('utf-8')
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post', kwargs={ 'pk': self.id })

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Page(models.Model):
    title = models.CharField(max_length=256, default='new page')
    slug = models.CharField(max_length=256, default='slug')
    raw = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content_html = models.TextField()
    author = models.ForeignKey(User)
    is_draft = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.content_html = markdown2.markdown(self.raw, extras=['code-friendly', 'fenced-code-blocks']).encode('utf-8')
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:page', kwargs={ 'pk': self.id })

@python_2_unicode_compatible
class BlogMeta(models.Model):
    key = models.CharField(max_length=256)
    value = models.CharField(max_length=256, null=True, blank=True)
    flag = models.BooleanField(default=False)
    misc = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.key

