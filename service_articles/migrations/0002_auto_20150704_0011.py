# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gnatology',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, max_length=5500)),
                ('date', models.DateField(blank=True, max_length=128)),
                ('image', models.ImageField(upload_to='images/', blank=True, max_length=200)),
                ('link', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Статьи по гнатологии',
                'verbose_name': 'Статью по гнатологии',
            },
        ),
        migrations.AlterModelOptions(
            name='cosmetology',
            options={'verbose_name_plural': 'Статьи по косметологии', 'verbose_name': 'Статью по косметологии'},
        ),
    ]
