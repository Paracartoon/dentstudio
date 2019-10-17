# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20150616_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workimage',
            old_name='number',
            new_name='work_number',
        ),
    ]
