#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256, default='new blog')
    abstract = models.TextField(null=True, blank=True)
    raw = models.TextField()
    date = models.DateTimeField(auto_now=True)
    content_html = models.TextField()
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag')
    catagory = models.ForeignKey('Catagory', null=True, blank=True)

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=256, default='new page')
    slug = models.CharField(max_length=256, default='slug')
    raw = models.TextField()
    date = models.DateTimeField(auto_now=True)
    content_html = models.TextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class BlogMeta(models.Model):
    title = models.CharField(max_length=256)
    misc = models.CharField(max_length=256)
    flag = models.CharField(max_length=256)

    def __unicode__(self):
        return self.flag + ":" + title

