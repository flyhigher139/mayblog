# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20150502_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'new blog', max_length=256)),
                ('abstract', models.TextField(null=True, blank=True)),
                ('raw', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('content_html', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, to='main.Category', null=True)),
                ('tags', models.ManyToManyField(to='main.Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
