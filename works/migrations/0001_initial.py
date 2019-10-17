# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000, blank=True)),
                ('link', models.CharField(max_length=128, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(max_length=200, upload_to='images/', blank=True)),
                ('work', models.ForeignKey(to='works.Work')),
            ],
        ),
    ]
