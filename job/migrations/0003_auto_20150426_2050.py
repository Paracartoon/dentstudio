# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_vacancy_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(max_length=2500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.TextField(max_length=2500, blank=True),
            preserve_default=True,
        ),
    ]
