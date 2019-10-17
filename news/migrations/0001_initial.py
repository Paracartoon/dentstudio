# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, max_length=128)),
                ('date', models.DateField(blank=True, max_length=128)),
                ('image', models.ImageField(blank=True, upload_to='images/', max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
