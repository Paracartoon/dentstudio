# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.TextField(max_length=2500, blank=True),
            preserve_default=True,
        ),
    ]
