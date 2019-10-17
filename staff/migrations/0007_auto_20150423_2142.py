# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_auto_20150423_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(max_length=200, upload_to='images/', blank=True),
            preserve_default=True,
        ),
    ]
