# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150612_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
    ]
