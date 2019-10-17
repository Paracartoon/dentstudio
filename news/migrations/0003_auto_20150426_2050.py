# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150424_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='new',
            name='shares',
        ),
        migrations.AddField(
            model_name='new',
            name='link',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
