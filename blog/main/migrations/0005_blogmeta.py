# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('misc', models.CharField(max_length=256)),
                ('flag', models.CharField(max_length=256)),
            ],
        ),
    ]
