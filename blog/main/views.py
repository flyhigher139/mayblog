#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_text
from django.db.models import Count, Q

from guardian.shortcuts import assign_perm, get_perms
from guardian.core import ObjectPermissionChecker
from guardian.decorators import permission_required

import markdown2

from . import models, forms, misc

# Create your views here.

PER_PAGE = settings.MAY_BLOG['PER_PAGE']
PER_PAGE_ADMIN = settings.MAY_BLOG['PER_PAGE_ADMIN']


def get_site_meta():
    seo = {}
    try:
        record = models.BlogMeta.objects.get(key='blog_name')
        seo['title'] = record.value
    except models.BlogMeta.DoesNotExist:
        pass

    try:
        record = models.BlogMeta.objects.get(key='blog_desc')
        seo['desc'] = record.value
    except models.BlogMeta.DoesNotExist:
        pass

    try:
        record = models.BlogMeta.objects.get(key='owner')
        seo['author'] = record.value
    except models.BlogMeta.DoesNotExist:
        pass

    try:
        record = models.BlogMeta.objects.get(key='keywords')
        seo['keywords'] = record.value
    except models.BlogMeta.DoesNotExist:
        pass

    try:
        record = models.BlogMeta.objects.get(key='blog_subtitle')
        seo['subtitle'] = record.value
    except models.BlogMeta.DoesNotExist:
        pass

    return seo

class Index(View):
    template_name = 'main/index.html'
    def get(self, request):
        data = {}
        
        tag = request.GET.get('tag')
        category = request.GET.get('category')
        try:
            tag = int(tag) if tag else 0
            category = int(category) if category else 0
        except:
            raise Http404

        if tag:
            posts = filter_posts_by_tag(tag)
        elif category:
            posts = filter_posts_by_category(category)
        else:
            posts = models.Post.objects.all()
        posts = posts.filter(is_draft=False).order_by('-id')
        post_pages = models.Page.objects.filter(is_draft=False)

        paginator = Paginator(posts, PER_PAGE)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)


        tags = models.Tag.objects.all()
        catagories = models.Category.objects.annotate(num_posts=Count('post'))

        data['posts'] = posts
        data['pages'] = post_pages
        data['tags'] = tags
        data['catagories'] = catagories
        data['category_id'] = category
        data['tag_id'] = tag

        data['seo'] = get_site_meta()

        return render(request, self.template_name, data)

class Post(View):
    template_name = 'main/post.html'
    def get(self, request, pk):
        try:
            pk = int(pk)
            post = models.Post.objects.get(pk=pk)
        except models.Post.DoesNotExist:
            raise Http404
        data = {'post':post}
        tags = post.tags.all()
        data['tags'] = tags

        comment_type = settings.MAY_BLOG['COMMENT_TYPE']
        comment_type_id = settings.MAY_BLOG['COMMENT_OPT'].get(comment_type)

        if not comment_type_id:
            comment_script = 'no comment script for {0}'.format(comment_type)
        else:
            comment_func = misc.get_comment_func(comment_type)
            # url_partial = [request.META['SERVER_NAME'], ':', request.META['SERVER_PORT'], request.path]
            # post_url = ''.join(url_partial)
            post_url = request.build_absolute_uri()
            comment_script = comment_func(request, comment_type_id, post.id, post.title, post_url)

        data['comment_script'] = comment_script

        seo = {
            'title': post.title, 
            'desc': post.abstract,
            'author': post.author.username,
            'keywords': ', '.join([tag.name for tag in tags])
        }

        data['seo'] = seo

        return render(request, self.template_name, data)

class Page(View):
    template_name = 'main/page.html'
    def get(self, request, pk):
        try:
            pk = int(pk)
            page = models.Page.objects.get(pk=pk)
        except models.Page.DoesNotExist:
            raise Http404
        data = {'page':page}
        data['seo'] = get_site_meta()

        return render(request, self.template_name, data)

class AdminIndex(View):
    template_name = 'blog_admin/index.html'
    @method_decorator(login_required)
    def get(self, request):
        data = {'site_info':get_site_meta()}
        return render(request, self.template_name, data)

class AdminBlogMeta(View):
    template_name = 'main/simple_form.html'
    @method_decorator(login_required)
    def get(self, request, form=None):
        if not form:
            form = forms.BlogMetaForm(initial=get_site_meta())

        data = {'form':form}
        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request):
        form = forms.BlogMetaForm(request.POST)
        if form.is_valid():
            record = models.BlogMeta.objects.get(key='blog_name')
            record.value = form.cleaned_data['title']
            record.save()

            record = models.BlogMeta.objects.get(key='blog_desc')
            record.value = form.cleaned_data['desc']
            record.save()
            
            record = models.BlogMeta.objects.get(key='owner')
            record.value = form.cleaned_data['author']
            record.save()
            
            record = models.BlogMeta.objects.get(key='keywords')
            record.value = form.cleaned_data['keywords']
            record.save()
            
            record = models.BlogMeta.objects.get(key='blog_subtitle')
            record.value = form.cleaned_data['subtitle']
            record.save()

            msg = 'Succeed to update blog meta'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('main:admin_index')

            return redirect(url)

            


        return self.get(request, form)

class AdminPosts(View):
    template_name_posts = 'blog_admin/posts.html'
    template_name_pages = 'blog_admin/pages.html'

    @method_decorator(login_required)
    def get(self, request, is_blog_page=False):
        data = {}
        draft = request.GET.get('draft')
        if draft and draft.lower()=='true':
            flag = True
        else:
            flag = False
        if is_blog_page:
            if not request.user.has_perm('main.change_page'):
                return HttpResponseForbidden()
            posts = models.Page.objects.all()
            template_name = self.template_name_pages
        else:
            posts = models.Post.objects.all()
            if not request.user.has_perm('main.change_post'):
                posts = posts.filter(author=request.user)
            template_name = self.template_name_posts

        posts = posts.filter(is_draft=flag)
        key = request.GET.get('key')
        if key:
            posts = posts.filter(Q(title__icontains=key)|Q(raw__icontains=key))
        posts = posts.order_by('-update_time')

        paginator = Paginator(posts, PER_PAGE_ADMIN)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        data['posts'] = posts
        data['is_blog_page'] = is_blog_page
        data['allow_search'] = True
        
        return render(request, template_name, data)

class AdminPost(View):
    template_name = 'blog_admin/post.html'

    # @method_decorator(login_required)
    @method_decorator(permission_required('main.add_post', accept_global_perms=True))
    def get(self, request, pk=0, form=None):
        data = {}
        form_data = {}
        if pk:
            try:
                pk = int(pk)
                post = models.Post.objects.get(pk=pk)
                
                #############################
                # It works! 
                #############################
                # if not 'change_post' in get_perms(request.user, post):
                #     raise HttpResponseForbidden()

                #############################
                # It works, too!
                #############################
                checker = ObjectPermissionChecker(request.user)
                if not request.user.has_perm('main.change_post') \
                    and not checker.has_perm('change_post', post):
                    return HttpResponse('Forbidden')

                form_data['title'] = post.title
                form_data['content'] = post.raw
                form_data['abstract'] = post.abstract
                data['edit_flag'] = True
            except models.Post.DoesNotExist:
                raise Http404
        else:
            post = None
        if not form:
            form = forms.NewPost(initial=form_data)
        data['form'] = form
        data['posted_tags'] = [tag for tag in post.tags.all()] if post else None
        data['posted_category'] = post.category if post else None
        tags = models.Tag.objects.all()
        data['tags'] = tags
        catagories = models.Category.objects.all()
        data['catagories'] = catagories
        return render(request, self.template_name, data)

    @method_decorator(permission_required('main.add_post', accept_global_perms=True))
    def post(self, request, pk=0, form=None):
        form = forms.NewPost(request.POST)
        if form.is_valid():
            if not pk:
                cur_post = models.Post()
            else:
                try:
                    pk = int(pk)
                    cur_post = models.Post.objects.get(pk=pk)
                    checker = ObjectPermissionChecker(request.user)
                    if not checker.has_perm('change_post', cur_post):
                        return HttpResponseForbidden('forbidden')
                except models.Post.DoesNotExist:
                    raise Http404
            cur_post.title = form.cleaned_data['title']
            cur_post.raw = form.cleaned_data['content']
            cur_post.abstract = form.cleaned_data['abstract']
            html = markdown2.markdown(cur_post.raw, extras=['code-friendly', 'fenced-code-blocks'])
            cur_post.content_html = smart_text(html)
            cur_post.author = request.user
            tag_ids = request.POST.getlist('tags')
            category_id = request.POST.get('category', None)
            # return HttpResponse(len(tag_ids))
            if request.POST.get('publish'):
                cur_post.is_draft = False
                
                msg = 'Post has been pulished!'
                messages.add_message(request, messages.SUCCESS, msg)
                url = reverse('main:admin_posts')

            else:
                cur_post.is_draft=True

                msg = 'Draft has been saved!'
                messages.add_message(request, messages.SUCCESS, msg)
                url = '{0}?draft=true'.format(reverse('main:admin_posts'))
                

            cur_post.category_id = category_id
            cur_post.save()
            cur_post.tags.clear()
            cur_post.tags.add(*tag_ids)

            assign_perm('main.change_post', request.user, cur_post)
            assign_perm('main.delete_post', request.user, cur_post)

            return redirect(url)

        return self.get(request, form)


class AdminPage(View):
    template_name = 'blog_admin/page.html'

    @method_decorator(permission_required('main.add_page', accept_global_perms=True))
    def get(self, request, pk=0, form=None):
        data = {}
        form_data = {}
        if pk:
            try:
                pk = int(pk)
                page = models.Page.objects.get(pk=pk)
                form_data['title'] = page.title
                form_data['content'] = page.raw
                form_data['slug'] = page.slug
                data['edit_flag'] = True
            except models.Post.DoesNotExist:
                raise Http404
        else:
            page = None
        if not form:
            form = forms.NewPage(initial=form_data)
        data['form'] = form

        return render(request, self.template_name, data)

    @method_decorator(permission_required('main.add_page', accept_global_perms=True))
    def post(self, request, pk=0, form=None):
        form = forms.NewPage(request.POST)
        if form.is_valid():
            if not pk:
                cur_post = models.Page()
            else:
                try:
                    pk = int(pk)
                    cur_post = models.Page.objects.get(pk=pk)
                except models.Page.DoesNotExist:
                    raise Http404
            cur_post.title = form.cleaned_data['title']
            cur_post.raw = form.cleaned_data['content']
            cur_post.slug = form.cleaned_data['slug']
            html = markdown2.markdown(cur_post.raw, extras=['code-friendly', 'fenced-code-blocks'])
            cur_post.content_html = smart_text(html)
            cur_post.author = request.user

            if request.POST.get('publish'):
                cur_post.is_draft = False
                
                msg = 'Page has been pulished!'
                messages.add_message(request, messages.SUCCESS, msg)
                url = reverse('main:admin_pages')

            else:
                cur_post.is_draft=True

                msg = 'Draft has been saved!'
                messages.add_message(request, messages.SUCCESS, msg)
                url = '{0}?draft=true'.format(reverse('main:admin_pages'))
                

            cur_post.save()

            return redirect(url)

        return self.get(request, form)


class DeletePost(View):
    @method_decorator(permission_required('main.delete_post', (models.Post, 'id', 'pk'), accept_global_perms=True))
    def get(self, request, pk):
        try:
            pk = int(pk)
            cur_post = models.Post.objects.get(pk=pk)
            is_draft = cur_post.is_draft

            # checker = ObjectPermissionChecker(request.user)
            # if not request.user.has_perm('main.delete_post') \
            #     and not checker.has_perm('delete_post', cur_post):
            #     return HttpResponse('forbidden')

            url = reverse('main:admin_posts')
            if is_draft:
                url = '{0}?draft=true'.format(url)    
            cur_post.delete()
        except models.Post.DoesNotExist:
            raise Http404

        return redirect(url)

class DeletePage(View):
    @method_decorator(permission_required('main.delete_page', accept_global_perms=True))
    def get(self, request, pk):
        try:
            pk = int(pk)
            cur_post = models.Page.objects.get(pk=pk)
            is_draft = cur_post.is_draft

            checker = ObjectPermissionChecker(request.user)
            if not checker.has_perm('delete_page', cur_post):
                # return HttpResponseForbidden('forbidden')
                return HttpResponse('forbidden')

            url = reverse('main:admin_pages')
            if is_draft:
                url = '{0}?draft=true'.format(url)    
            cur_post.delete()
        except models.Page.DoesNotExist:
            raise Http404

        return redirect(url)

        
class AdminTags(View):
    template_name = 'blog_admin/tags.html'

    @method_decorator(login_required)
    def get(self, request, form=None):
        if not form:
            form = forms.TagForm()
        tags = models.Tag.objects.all()

        paginator = Paginator(tags, PER_PAGE_ADMIN)
        page = request.GET.get('page')

        try:
            tags = paginator.page(page)

        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)


        data = {'tags':tags, 'form':form}

        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request, form=None):
        form = forms.TagForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                tag_model, created = models.Tag.objects.get_or_create(name=tag)

            msg = 'Succeed to create tags'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('main:admin_tags')
            return redirect(url)
        else:
            return self.get(request, form=form)

class AdminCategory(View):
    template_name = 'blog_admin/category.html'

    @method_decorator(login_required)
    def get(self, request, form=None):
        if not form:
            form = forms.CategoryForm()
        catagories = models.Category.objects.all()
        paginator = Paginator(catagories, PER_PAGE_ADMIN)
        page = request.GET.get('page')
        try:
            catagories = paginator.page(page)
        except PageNotAnInteger:
            catagories = paginator.page(1)
        except EmptyPage:
            catagories = paginator.page(paginator.num_pages)

        data = {'catagories':catagories, 'form':form}

        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request, form=None):
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            category = models.Category()
            category.name = form.cleaned_data['name']
            category.save()

            msg = 'Succeed to create new category'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('main:admin_category')
            return redirect(url)
        else:
            return self.get(request, form=form)

class AdminFilterPosts(View):
    template_name = 'blog_admin/posts.html'

    @method_decorator(login_required)
    def get(self, request):
        tag_id = request.GET.get('tag')
        category_id = request.GET.get('category')

        if tag_id:
            posts = filter_posts_by_tag(tag_id)
        elif category_id:
            posts = filter_posts_by_category(category_id)
        else:
            url = reverse('main:admin_posts')
            return redirect(url)

        if posts == None:
            raise Http404

        paginator = Paginator(posts, PER_PAGE_ADMIN)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        data = {'posts':posts}
        return render(request, self.template_name, data)

def filter_posts_by_tag(pk):
    try:
        tag = models.Tag.objects.get(pk=pk)
    except models.Tag.DoesNotExist:
        return None

    posts = tag.post_set.all()
    return posts

def filter_posts_by_category(pk):
    try:
        category = models.Category.objects.get(pk=pk)
    except models.Category.DoesNotExist:
        return None

    posts = category.post_set.all()
    return posts

