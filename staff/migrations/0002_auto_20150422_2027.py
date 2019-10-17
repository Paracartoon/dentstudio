# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='description',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
