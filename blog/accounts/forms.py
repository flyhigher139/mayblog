#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

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