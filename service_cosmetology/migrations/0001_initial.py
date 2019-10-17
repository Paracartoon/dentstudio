# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Cosmetology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, max_length=5500)),
                ('date', models.DateField(blank=True, max_length=128)),
                ('image', models.ImageField(blank=True, max_length=200, upload_to='images/')),
                ('link', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
