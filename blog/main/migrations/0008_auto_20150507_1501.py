# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150506_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='update_time',
        ),
        migrations.AddField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 15, 1, 13, 50985, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
