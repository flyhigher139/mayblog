#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from accounts import forms
from . import models

def init_blog(request):
    # Create superuser
    # get_user_model().objects.create_superuser(username='su', email='su@email.com', password='su')
    try:
        su = User.objects.get(username='su')
    except User.DoesNotExist:
        User.objects.create_superuser(username='su', email='su@email.com', password='su')
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

class BlogInitView(View):
    template_name = 'main/simple_form.html'
    def get(self, request, form=None):
        initialized = False

        try:
            initialization = models.BlogMeta.objects.get(key='initialization')
            initialized = initialization.flag
        except models.BlogMeta.DoesNotExist:
            initialized = False
        
        if initialized:
            url = reverse('main:admin_index')
            return redirect(url)


        if not form:
            form = forms.RegisterForm()
        data = {'form':form}
        data['title'] = 'System Initialization'
        data['heading'] = 'Create Superuser'
        return render(request, self.template_name, data)

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_superuser(username, email, password)


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

            initialization, created = models.BlogMeta.objects.get_or_create(key='initialization')
            initialization.flag = True
            initialization.save()

            # obj = models.BlogMeta()
            # obj.key = 'blog_name'
            # obj.value = 'MayBlog'
            # obj.save()

            obj, created = models.BlogMeta.objects.get_or_create(key='blog_name', defaults={'value':'MayBlog'})

            # # obj = models.BlogMeta()
            # # obj.key = 'blog_subtitle'
            # # obj.value = 'Welcome to MayBlog'
            # # obj.save()

            obj, created = models.BlogMeta.objects.get_or_create(key='blog_subtitle', defaults={'value':'Welcome to MayBlog'})
            obj, created = models.BlogMeta.objects.get_or_create(key='blog_desc', defaults={'value':'desc'})
            obj, created = models.BlogMeta.objects.get_or_create(key='owner', defaults={'value':'MayBlog'})
            obj, created = models.BlogMeta.objects.get_or_create(key='keywords', defaults={'value':'MayBlog'})

            msg = 'Successfully Initialized'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('main:admin_index')
            return redirect(url)

        else:
            return self.get(request, form)

def create_admin_group():
    group, created = Group.objects.get_or_create(name='administrator')
    codenames = [
        'add_user', 'change_user', 'delete_user',
        'add_blogmeta', 'change_blogmeta', 'delete_blogmeta',
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