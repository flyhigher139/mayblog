#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse

from . import models

def init_blog(request):
    # Create admin group
    group = create_admin_group()

    # Create editor group
    group = create_editor_group()

    # Create writer group
    group = create_writer_group()

    # Create contributor group
    group = create_contributor_group()

    # Create reader group
    group = create_reader_group()


    # Create default category
    default_category, created = models.Category.objects.get_or_create(name='default')

    return HttpResponse('succeed to init blog')

def create_admin_group():
    group, created = Group.objects.get_or_create(name='administrator')
    codenames = [
        'add_user', 'change_user', 'delete_user',
        'add_post', 'change_post', 'delete_post', 
        'add_page', 'change_page', 'delete_page',
        'add_category', 'change_category', 'delete_category',
        'add_tag', 'change_tag', 'delete_tag',
    ]

    permissions = Permission.objects.filter(codename__in=codenames)
    group.permissions = permissions


    return group

def create_editor_group():
    group, created = Group.objects.get_or_create(name='editor')
    codenames = [
        'add_post', 'change_post', 'delete_post', 
        'add_page', 'change_page', 'delete_page',
        'add_category', 'change_category', 'delete_category',
        'add_tag', 'change_tag', 'delete_tag',

    ]

    permissions = Permission.objects.filter(codename__in=codenames)
    group.permissions = permissions


    return group

def create_writer_group():
    group, created = Group.objects.get_or_create(name='writer')
    codenames = [
        'add_post', #'change_post', 'delete_post', 
        #'add_page', 'change_page', 'delete_page',
        #'add_category', 'change_category', 'delete_category',
        'add_tag', #'change_tag', 'delete_tag',

    ]

    permissions = Permission.objects.filter(codename__in=codenames)
    group.permissions = permissions


    return group

def create_contributor_group():
    group, created = Group.objects.get_or_create(name='contributor')
    codenames = [
        'add_post', #'change_post', 'delete_post', 
        #'add_page', 'change_page', 'delete_page',
        #'add_category', 'change_category', 'delete_category',
        #'add_tag', 'change_tag', 'delete_tag',

    ]

    permissions = Permission.objects.filter(codename__in=codenames)
    group.permissions = permissions


    return group

def create_reader_group():
    group, created = Group.objects.get_or_create(name='reader')
    codenames = [
        # 'add_post', 'change_post', 'delete_post', 
        # 'add_page', 'change_page', 'delete_page',
        # 'add_category', 'change_category', 'delete_category',
        # 'add_tag', 'change_tag', 'delete_tag',

    ]

    permissions = Permission.objects.filter(codename__in=codenames)
    group.permissions = permissions


    return group