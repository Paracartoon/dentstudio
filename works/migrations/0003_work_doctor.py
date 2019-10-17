# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20150616_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='doctor',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
