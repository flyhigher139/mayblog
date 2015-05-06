#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.views.generic import View
from django.shortcuts import render

import markdown2

from . import models, forms

# Create your views here.

class Index(View):
    template_name = 'main/index.html'
    def get(self, request):
        data = {}
        posts = models.Post.objects.all()
        pages = models.Page.objects.all()
        data['posts'] = posts
        data['pages'] = pages
        return render(request, self.template_name, data)

class Post(View):
    template_name = 'main/post.html'
    def get(self, request, pk):
        try:
            post = models.Post.objects.get(pk=pk)
        except post.DoesNotExist:
            raise Http404
        data = {'post':post}
        return render(request, self.template_name, data)

class Page(View):
    template_name = 'main/page.html'
    def get(self, request, pk):
        try:
            page = models.Page.objects.get(pk=pk)
        except page.DoesNotExist:
            raise Http404
        data = {'page':page}
        return render(request, self.template_name, data)

class AdminIndex(View):
    template_name = 'blog_admin/index.html'
    def get(self, request):
        data = {}
        return render(request, self.template_name, data)

class AdminPosts(View):
    template_name = 'blog_admin/index.html'
    def get(self, request):
        data = {}
        return render(request, self.template_name, data)

class AdminPost(View):
    template_name = 'blog_admin/post.html'
    def get(self, request, form=None):
        data = {}
        if not form:
            form = forms.NewPost()
        data['form'] = form
        return render(request, self.template_name, data)

    def post(self, request):
        form = forms.NewPost(request.POST)
        if form.is_valid():
            cur_post = models.Post()
            cur_post.title = form.cleaned_data['title']
            cur_post.raw = form.cleaned_data['content']
            cur_post.abstract = form.cleaned_data['abstract']
            html = markdown2.markdown(cur_post.raw, extras=['code-friendly', 'fenced-code-blocks'])
            cur_post.content_html = html
            cur_post.author = request.user
            cur_post.save()
            return HttpResponse('post has been saved and pulished!')

        return self.get(request, form)
        





