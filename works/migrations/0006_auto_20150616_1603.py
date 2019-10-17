# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20150616_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='main_image',
            new_name='main_image1',
        ),
        migrations.AddField(
            model_name='work',
            name='main_image2',
            field=models.ImageField(upload_to='images/', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='work',
            name='main_image3',
            field=models.ImageField(upload_to='images/', max_length=200, blank=True),
        ),
    ]
