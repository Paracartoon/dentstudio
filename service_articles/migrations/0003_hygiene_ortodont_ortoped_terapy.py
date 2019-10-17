# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_articles', '0002_auto_20150704_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hygiene',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, blank=True, upload_to='images/')),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи по профгигиене',
                'verbose_name': 'Статью по профгигиене',
            },
        ),
        migrations.CreateModel(
            name='Ortodont',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, blank=True, upload_to='images/')),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи по ортодонтии',
                'verbose_name': 'Статью по ортодонтии',
            },
        ),
        migrations.CreateModel(
            name='Ortoped',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, blank=True, upload_to='images/')),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи по ортопедии',
                'verbose_name': 'Статью по ортопедии',
            },
        ),
        migrations.CreateModel(
            name='Terapy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=5500, blank=True)),
                ('date', models.DateField(max_length=128, blank=True)),
                ('image', models.ImageField(max_length=200, blank=True, upload_to='images/')),
                ('link', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи по терапии',
                'verbose_name': 'Статью по терапии',
            },
        ),
    ]
