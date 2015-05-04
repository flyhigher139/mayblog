#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class NewPost(forms.Form):
    title = forms.CharField(max_length=256)
    content = forms.TextField()
    abstruct = forms.TextField()
    tag = forms.CharField(max_length=256)
    catagory = forms.CharField(max_length=256)