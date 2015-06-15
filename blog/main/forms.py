#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class NewPost(forms.Form):
    title = forms.CharField(max_length=256)
    content = forms.CharField(widget=forms.Textarea)
    abstract = forms.CharField(widget=forms.Textarea)
    # tag = forms.CharField(max_length=256, required=False)
    # category = forms.CharField(max_length=256, required=False)

class NewPage(forms.Form):
    title = forms.CharField(max_length=256)
    slug = forms.CharField(max_length=64)
    content = forms.CharField(widget=forms.Textarea)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=256, label='Category Name')

class TagForm(forms.Form):
    tags = forms.CharField(max_length=256, label='Tags')