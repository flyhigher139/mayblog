from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin2/', include(admin.site.urls)),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/', include('api.urls', namespace='api')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
