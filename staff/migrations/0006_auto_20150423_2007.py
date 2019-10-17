# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20150423_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='file',
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to='images/', blank=True),
            preserve_default=True,
        ),
    ]
