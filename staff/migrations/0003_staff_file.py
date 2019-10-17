# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150422_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='file',
            field=models.FileField(blank=True, upload_to='/static/'),
            preserve_default=True,
        ),
    ]
