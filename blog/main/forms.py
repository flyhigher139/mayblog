#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class NewPost(forms.Form):
    title = forms.CharField(max_length=256)
    content = forms.CharField(widget=forms.Textarea)
    abstract = forms.CharField(widget=forms.Textarea)
    # tag = forms.CharField(max_length=256, required=False)
    # catagory = forms.CharField(max_length=256, required=False)