#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256, default='new blog')
    abstract = models.TextField(null=True, blank=True)
    raw = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content_html = models.TextField()
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag')
    category = models.ForeignKey('Category', null=True, blank=True)
    is_draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=256, default='new page')
    slug = models.CharField(max_length=256, default='slug')
    raw = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content_html = models.TextField()
    author = models.ForeignKey(User)
    is_draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class BlogMeta(models.Model):
    value = models.CharField(max_length=256)
    flag = models.BooleanField(default=False)
    misc = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.value + ":" + str(self.flag)

