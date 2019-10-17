# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20150427_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'persons'},
        ),
    ]
