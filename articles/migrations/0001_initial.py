# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(upload_to='images/', max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
