# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20150605_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
