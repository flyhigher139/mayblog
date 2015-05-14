#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View

from . import forms

# Create your views here.
class LoginView(View):
    template_name = 'accounts/login.html'
    def get(self, request, form=None):
        data = {}
        if not form:
            form = forms.LoginForm()
        data['form'] = form
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

