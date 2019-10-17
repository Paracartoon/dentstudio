# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150426_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='id',
        ),
        migrations.AlterField(
            model_name='new',
            name='link',
            field=models.CharField(serialize=False, primary_key=True, max_length=128),
        ),
    ]
