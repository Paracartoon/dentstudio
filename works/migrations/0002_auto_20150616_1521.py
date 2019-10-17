# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workimage',
            name='desc',
            field=models.TextField(blank=True, max_length=2500),
        ),
        migrations.AddField(
            model_name='workimage',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
