# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150612_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='link',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
