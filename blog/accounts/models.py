#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Account(models.Model):
    display_name = models.CharField(max_length=128)
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

    def __str__(self):
        return self.display_name

@python_2_unicode_compatible
class SocialInfo(models.Model):
    SOCIAL_CHOICES = (
    ('fa-facebook', 'Facebook'),
    ('fa-github', 'Github'),
    ('fa-twitter', 'Twitter'),
    ('fa-google-plus', 'Google Plus'),
    ('fa-weibo', 'Weibo'),)
    ('fa-bookmark', 'Other'),

    user = models.ForeignKey(User)
    social = models.CharField(choices=SOCIAL_CHOICES, max_length=128)
    url = models.URLField()

    def __str__(self):
        return self.user.name + '-' + self.social
