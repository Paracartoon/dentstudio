# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmetology',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, upload_to='images/', blank=True)),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name': 'Косметология',
                'verbose_name_plural': 'Статьи по косметологии',
            },
        ),
    ]
