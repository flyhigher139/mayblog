from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Post, BlogMeta
from .views import get_site_meta

# def get_site_meta():
#     seo = {}
#     try:
#         record = BlogMeta.objects.get(key='blog_name')
#         seo['title'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='blog_desc')
#         seo['desc'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='owner')
#         seo['author'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='keywords')
#         seo['keywords'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='blog_subtitle')
#         seo['subtitle'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='google_verify')
#         seo['google_verify'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     try:
#         record = BlogMeta.objects.get(key='baidu_verify')
#         seo['baidu_verify'] = record.value
#     except BlogMeta.DoesNotExist:
#         pass

#     return seo

# META_DATA = get_site_meta()
FEED_NUM = settings.MAY_BLOG['RSS_NUM']


# class LatestEntriesFeed(Feed):
#     feed_type = Atom1Feed

#     # title = "MayBlog"
#     # link = "/"
#     description = "MayBlog Rss"

#     def get_object(self, request, pk):
#         # return get_object_or_404(Post, pk=id)
#         return Post.objects.get(pk=pk)

#     def title(self, obj):
#         return "MayBlog: %s posts" % obj.title

#     def link(self, item):
#         return reverse('main:post', args=[item.pk])
#         # return '/'

#     def items(self):
#         return Post.objects.filter(is_draft=False)

#     def item_title(self, item):
#         return item.title

#     def item_description(self, item):
#         return item.content_html

#     # item_link is only needed if Post has no get_absolute_url method.
#     def item_link(self, item):
#         return reverse('main:post', args=[item.pk])
#         # return '/'

class LatestEntriesFeed2(Feed):


    def title(self):
        META_DATA = get_site_meta()
        return META_DATA.get('title')

    def link(self, item):
        return reverse('main:rss')
        # return '/rss/'

    def description(self):
        META_DATA = get_site_meta()
        return META_DATA.get('subtitle')

    def items(self):
        return Post.objects.filter(is_draft=False).order_by('-update_time')[:FEED_NUM]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('main:post', args=[item.pk])

    