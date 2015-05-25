# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150507_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
