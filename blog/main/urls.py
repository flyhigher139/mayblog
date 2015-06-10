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
    url(r'^admin/pages$', views.AdminPosts.as_view(), {'is_blog_page':True}, name='admin_pages'),
    url(r'^admin/post$', views.AdminPost.as_view(), name='admin_post'),
    url(r'^admin/page$', views.AdminPage.as_view(), name='admin_page'),
    url(r'^admin/posts/(?P<pk>[0-9]+)$', views.AdminPost.as_view(), name='admin_edit_post'),
    url(r'^admin/pages/(?P<pk>[0-9]+)$', views.AdminPage.as_view(), name='admin_edit_page'),
    url(r'^admin/posts/delete/(?P<pk>[0-9]+)$', views.DeletePost.as_view(), name='admin_delete_post'),
    url(r'^admin/pages/delete/(?P<pk>[0-9]+)$', views.DeletePage.as_view(), name='admin_delete_page'),
    url(r'^admin/tags/$', views.AdminTags.as_view(), name='admin_tags'),
    url(r'^admin/category/$', views.AdminCategory.as_view(), name='admin_category'),
    url(r'^admin/filter-posts$', views.AdminFilterPosts.as_view(), name='admin_filter_posts'),
)