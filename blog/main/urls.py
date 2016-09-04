#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from . import views, preblog, feeds, sitemaps


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.Post.as_view(), name='post'),
    url(r'^page/(?P<pk>[0-9]+)/$', views.Page.as_view(), name='page'),
    url(r'^archive$', views.Archive.as_view(), name='archive'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.Author.as_view(), name='author'),
]

urlpatterns += [
    url(r'^admin/$', views.AdminIndex.as_view(), name='admin_index'),
    url(r'^admin/meta$', views.AdminBlogMeta.as_view(), name='admin_blog_meta'),
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
    url(r'^admin/tags/delete/(?P<pk>[0-9]+)$', views.simple_delete, {'flag':'tag'}, name='admin_delete_tag'),
    url(r'^admin/categories/delete/(?P<pk>[0-9]+)$', views.simple_delete, {'flag':'category'}, name='admin_delete_category'),
    url(r'^admin/tags/edit/(?P<pk>[0-9]+)$', views.simple_update, {'flag':'tag'}, name='admin_edit_tag'),
    url(r'^admin/categories/edit/(?P<pk>[0-9]+)$', views.simple_update, {'flag':'category'}, name='admin_edit_category'),
]

urlpatterns += [
    url(r'^init$', preblog.BlogInitView.as_view()),
    url(r'^reinit-meta$', preblog.ReInitBlogMetaView.as_view()),
    url(r'^rss/$', feeds.LatestEntriesFeed2(), name='rss'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps.sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]



