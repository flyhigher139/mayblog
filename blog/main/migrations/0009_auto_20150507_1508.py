# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150507_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='date',
            new_name='update_time',
        ),
        migrations.AddField(
            model_name='page',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 15, 8, 25, 70301, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
