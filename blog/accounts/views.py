#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from django.conf import settings

from . import forms

PER_PAGE = settings.MAY_BLOG['PER_PAGE_ADMIN']

# Create your views here.
class LoginView(View):
    template_name = 'accounts/simple_form.html'
    def get(self, request, form=None):
        data = {}
        if not form:
            form = forms.LoginForm()
        data['form'] = form
        data['title'] = 'Login'
        data['btn_name'] = 'Login'
        return render(request, self.template_name, data)
    def post(self, request, form=None):
        data = {}
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    url = request.GET.get('next', None)
                    if not url:
                        url = reverse('main:admin_index')
                    return redirect(url)
                else:
                    # Return a 'disabled account' error message
                    msg = 'The user is disabled'
                    messages.add_message(request, messages.WARNING, msg)
                    return self.get(request, form)
            else:
                # Return an 'invalid login' error message.
                msg = 'Invalid login, user does not exist'
                messages.add_message(request, messages.ERROR, msg)
                return self.get(request, form)

        else:
            return self.get(request, form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        msg = 'Succeed to logout'
        url = reverse('accounts:login')
        return redirect(url)

class RegisterView(View):
    template_name = 'accounts/simple_form.html'
    def get(self, request, form=None):
        if not form:
            form = forms.RegisterForm()

        data = {'title':'Register', 'form':form, 'btn_name':'Register'}

        return render(request, self.template_name, data)

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username, email, password)
            
            user.save()

            msg = 'Successfully Registered'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('accounts:login')
            return redirect(url)

        else:
            return self.get(request, form)

class UsersView(View):
    template_name = 'accounts/users.html'
    def get(self, request):
        users = User.objects.all()
        paginator = Paginator(users, PER_PAGE)
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        data = {'users':users}

        return render(request, self.template_name, data)

class GroupView(View):
    template_name = 'accounts/groups.html'
    def get(self, request):
        groups = Group.objects.all()
        data = {'groups':groups}

        return render(request, self.template_name, data)



