#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class NewPost(forms.Form):
    title = forms.CharField(max_length=256)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':20}))
    abstract = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    author_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    # tag = forms.CharField(max_length=256, required=False)
    # category = forms.CharField(max_length=256, required=False)

class NewPage(forms.Form):
    title = forms.CharField(max_length=256)
    slug = forms.CharField(max_length=64)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':20}))
    author_id = forms.IntegerField(required=False, widget=forms.HiddenInput)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=256, label='Category Name')

class TagForm(forms.Form):
    tags = forms.CharField(max_length=256, label='Tags')

class BlogMetaForm(forms.Form):
    title = forms.CharField(max_length=256, label='Title')
    subtitle = forms.CharField(max_length=256, label='SubTitle')
    desc = forms.CharField(max_length=256, label='Description')
    author = forms.CharField(max_length=256, label='Owner')
    keywords = forms.CharField(max_length=256, label='Keywords')
    google_verify = forms.CharField(max_length=256, label='Google Site Verification', required=False)
    baidu_verify = forms.CharField(max_length=256, label='Baidu Site Verification', required=False)