# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='file',
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
            preserve_default=True,
        ),
    ]
