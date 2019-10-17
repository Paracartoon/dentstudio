# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_work_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='workimage',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
