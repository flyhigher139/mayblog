#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext, loader

def get_comment_func(comment_type):
    if comment_type == 'duoshuo':
        return duoshuo_comment
    else:
        return None

def duoshuo_comment(request, duoshuo_id, post_id, post_title, post_url):
    '''
    Create duoshuo script by params
    '''
    template_name = 'main/misc/duoshuo.html'

    template = loader.get_template(template_name)
    data = {
        'duoshuo_id': duoshuo_id,
        'post_id': post_id,
        'post_title': post_title,
        'post_url': post_url,
    }
    context = RequestContext(request, data)
    return template.render(context)