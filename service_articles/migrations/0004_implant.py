# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_articles', '0003_hygiene_ortodont_ortoped_terapy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, max_length=5500)),
                ('date', models.DateField(blank=True, max_length=128)),
                ('image', models.ImageField(upload_to='images/', blank=True, max_length=200)),
                ('link', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Статьи по имплантологии',
                'verbose_name': 'Статью по имплантологии',
            },
        ),
    ]
