#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class Account(models.Model):
    display_name = models.CharField(max_length='128')
    biography = models.TextField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    weixin = models.URLField(null=True, blank=True)
    douban = models.URLField(null=True, blank=True)
    weibo = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    user = models.OneToOneField(User)


    @receiver(post_save, sender=User)
    def create_user_account(sender, instance=None, created=False, **kwargs):
        if created:
            Account.objects.get_or_create(user=instance, defaults={'display_name':instance.username})

    def __unicode__(self):
        return self.display_name

class SocialInfo(models.Model):
    SOCIAL_CHOICES = (
    ('fa-facebook', 'Facebook'),
    ('fa-github', 'Github'),
    ('fa-twitter', 'Twitter'),
    ('fa-google-plus', 'Google Plus'),
    ('fa-weibo', 'Weibo'),)
    ('fa-bookmark', 'Other'),

    user = models.ForeignKey(User)
    social = models.CharField(choices=SOCIAL_CHOICES, max_length='128')
    url = models.URLField()

    def __unicode__(self):
        return user.name + '-' + social
