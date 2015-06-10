# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_page_is_draft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmeta',
            old_name='title',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='blogmeta',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogmeta',
            name='misc',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
