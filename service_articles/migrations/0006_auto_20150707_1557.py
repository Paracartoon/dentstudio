# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_articles', '0005_parodontology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmetology',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='gnatology',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='hygiene',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='implant',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='ortodont',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='ortoped',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='parodontology',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
        migrations.AlterField(
            model_name='terapy',
            name='text',
            field=models.TextField(blank=True, max_length=555500),
        ),
    ]
