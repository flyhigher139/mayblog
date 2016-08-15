#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categories$', views.CategoryListView.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)$', views.CategoryDetailView.as_view()),
    url(r'^tags$', views.TagListView.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetailView.as_view(), name='api_tag'),
    url(r'^posts$', views.PostListView.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetailView.as_view()),
]

