#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group

def group_values():
    groups = Group.objects.all()
    choices = [(group.id, group.name) for group in groups ]
    return choices

class LoginForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256, required=False)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=256, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Two passwords are not the same')

class UserForm(forms.Form):
    username = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256, required=False)
    # password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'placeholder': 'password'}), required=False)
    # password_confirm = forms.CharField(max_length=256, widget=forms.PasswordInput)
    # is_staff = forms.BooleanField(required=False)
    # is_superuser = forms.BooleanField(required=False)

    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     password = cleaned_data.get('password')
    #     password_confirm = cleaned_data.get('password_confirm')
    #     if password != password_confirm:
    #         raise forms.ValidationError('Two passwords are not the same')

class UserGroupForm(forms.Form):
    # GROUP_CHOICES = group_values()
    GROUP_CHOICES = ()
    groups = forms.MultipleChoiceField(choices=GROUP_CHOICES, widget=forms.SelectMultiple(attrs={'size':len(GROUP_CHOICES)}))

    def __init__(self, *args, **kwargs):
        super(UserGroupForm, self).__init__(*args, **kwargs)
        groups = [(group.id, group.name) for group in Group.objects.all() ]
        # self.fields['groups'].choices = groups
        # self.fields['groups'].widget = forms.SelectMultiple(attrs={'size':len(groups)})
        self.fields['groups'] = forms.MultipleChoiceField(choices=groups, widget=forms.SelectMultiple(attrs={'size':len(groups)}))


    

