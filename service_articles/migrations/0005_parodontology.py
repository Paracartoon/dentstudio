# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_articles', '0004_implant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parodontology',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, upload_to='images/', blank=True)),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name': 'Статью по пародонтологии',
                'verbose_name_plural': 'Статьи по пародонтологии',
            },
        ),
    ]
