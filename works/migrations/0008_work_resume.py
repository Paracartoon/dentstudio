# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0007_auto_20150616_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='resume',
            field=models.TextField(blank=True, max_length=2500),
        ),
    ]
