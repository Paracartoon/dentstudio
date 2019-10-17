# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_workimage_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='main_image',
            field=models.ImageField(blank=True, max_length=200, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='workimage',
            name='image',
            field=models.ImageField(blank=True, max_length=900, upload_to='images/'),
        ),
    ]
