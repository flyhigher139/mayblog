#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)$', views.Post.as_view(), name='post'),
    url(r'^page/(?P<pk>[0-9]+)$', views.Page.as_view(), name='page'),)

urlpatterns += patterns('',
    url(r'^admin/$', views.AdminIndex.as_view(), name='admin_index'),
    url(r'^admin/posts$', views.AdminPosts.as_view(), name='admin_posts'),
    url(r'^admin/post$', views.AdminPost.as_view(), name='admin_post'),
)