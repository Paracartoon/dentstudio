# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email_address',
            field=models.EmailField(null=True, blank=True, max_length=75),
            preserve_default=True,
        ),
    ]
