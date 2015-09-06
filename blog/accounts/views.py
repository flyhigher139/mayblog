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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from guardian.decorators import permission_required

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

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def get(self, request, group_id=0):
        data = {}
        
        if group_id:
            group = Group.objects.get(pk=group_id)
            users = group.user_set.all()
            data['group_id'] = int(group_id)
        else:
            users = User.objects.all()
            data['all'] = True

        key = request.GET.get('key')
        if key:
            users = users.filter(username__icontains=key)

        paginator = Paginator(users, PER_PAGE)
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        groups = Group.objects.all()
        # data = {'users':users, 'groups':groups}
        data['users'] = users
        data['groups'] = groups

        data['allow_search'] = True

        return render(request, self.template_name, data)

class UserView(View):
    template_name = 'accounts/user.html'

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def get(self, request, pk):
        pk = int(pk)
        data = {}
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        data['user'] = user

        groups = user.groups.all()
        data['groups'] = groups

        # permissions = user.get_all_permissions()
        # data['permissions'] = permissions
        permissions = user.user_permissions.all()
        data['permissions'] = permissions

        return render(request, self.template_name, data)

class GroupView(View):
    template_name = 'accounts/group.html'

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def get(self, request, pk):
        pk = int(pk)
        data = {}
        try:
            group = Group.objects.get(pk=pk)
        except group.DoesNotExist:
            raise Http404
        data['group'] = group

        permissions = group.permissions.all()
        data['permissions'] = permissions

        users = group.user_set.all()
        data['users'] = users

        return render(request, self.template_name, data)

class UserEditView(View):
    template_name = 'accounts/user_edit.html'

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def get(self, request, pk, user_form=None):
        pk = int(pk)
        data = {}
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
        data['user_edited'] = user

        user_dict = {'username':user.username, 'email': user.email}
        if not user_form:
            user_form = forms.UserForm(initial=user_dict)
        data['user_form'] = user_form

        groups = user.groups.all()
        user_groups = [group.id for group in groups ]
        group_dict = {'groups':user_groups}
        user_group_form = forms.UserGroupForm(initial=group_dict)
        data['user_group_form'] = user_group_form

        return render(request, self.template_name, data)

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def post(self, request, pk):
        pk = int(pk)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        if request.POST.get('user'):
            form = forms.UserForm(request.POST)
            if form.is_valid():
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                if request.user.is_superuser:
                    user.is_superuser = request.POST.get('is_superuser', False)
                    user.is_staff = request.POST.get('is_staff', False)
                user.save()

                url = reverse('accounts:user_edit', args=(pk,))
                msg = 'Succeed to update user details'
                messages.add_message(request, messages.SUCCESS, msg)
                return redirect(url)

            return self.get(request, pk, user_form=form)
        else:
            group_ids = request.POST.getlist('groups')
            # user.groups.add(*group_ids)
            user.groups = group_ids
            # return HttpResponse(group_ids)
            url = reverse('accounts:user_edit', args=(pk,))
            msg = 'Succeed to update user groups'
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect(url)


class GroupsView(View):
    template_name = 'accounts/groups.html'

    @method_decorator(permission_required('main.change_user', accept_global_perms=True))
    def get(self, request):
        groups = Group.objects.all()
        data = {'groups':groups}

        return render(request, self.template_name, data)

class ProfileView(View):
    template_name = 'accounts/settings_profile.html'

    @method_decorator(login_required)
    def get(self, request, form=None):
        data = {}
        form_data = {
            'display_name' : request.user.account.display_name,
            'biography' : request.user.account.biography,
            'homepage' : request.user.account.homepage,
            'weixin' : request.user.account.weixin,
            'douban' : request.user.account.douban,
            'weibo' : request.user.account.weibo,
            'twitter' : request.user.account.twitter,
            'github' : request.user.account.github
        }

        if not form:
            form = forms.ProfileForm(initial=form_data)

        data['form'] = form
        data['is_profile'] = True

        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request):
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            account = request.user.account

            account.display_name = form.cleaned_data['display_name']
            account.biography = form.cleaned_data['biography']
            account.homepage = form.cleaned_data['homepage']
            account.weixin = form.cleaned_data['weixin']
            account.douban = form.cleaned_data['douban']
            account.weibo = form.cleaned_data['weibo']
            account.twitter = form.cleaned_data['twitter']
            account.github = form.cleaned_data['github']

            account.save()

            msg = 'Succeed to update profile'
            url = reverse('accounts:profile')
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect(url)

        return self.get(request, form)

class ChangePasswordView(View):
    template_name = 'accounts/settings_profile.html'

    @method_decorator(login_required)
    def get(self, request, form=None):
        data = {}
        if not form:
            form = forms.ChangePasswordForm(initial={'username':request.user.username})

        data['form'] = form
        data['is_password'] = True

        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request):
        form = forms.ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(password)

            user.save()

            msg = 'Succeed to update profile'
            url = reverse('accounts:change_password')
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect(url)

        return self.get(request, form)





