# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150610_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmeta',
            name='key',
            field=models.CharField(default='key', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogmeta',
            name='value',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
