# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20150423_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='image',
        ),
        migrations.AddField(
            model_name='staff',
            name='file',
            field=models.FileField(blank=True, upload_to='images/'),
            preserve_default=True,
        ),
    ]
