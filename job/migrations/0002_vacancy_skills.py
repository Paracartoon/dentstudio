# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
