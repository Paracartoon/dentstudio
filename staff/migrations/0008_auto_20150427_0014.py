# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20150423_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='likes',
        ),
        migrations.AddField(
            model_name='staff',
            name='link',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(max_length=2500, blank=True),
            preserve_default=True,
        ),
    ]
