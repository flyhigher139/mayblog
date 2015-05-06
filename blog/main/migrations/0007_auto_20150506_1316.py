# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_is_draft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='pub_date',
        ),
    ]
