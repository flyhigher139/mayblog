from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Post
from .views import get_site_meta

META_DATA = get_site_meta()
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
        return META_DATA['title']

    def link(self, item):
        return reverse('main:rss')
        # return '/rss/'

    def description(self):
        return META_DATA['subtitle']

    def items(self):
        return Post.objects.filter(is_draft=False).order_by('-update_time')[:FEED_NUM]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('main:post', args=[item.pk])

    