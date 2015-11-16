# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pycon.sponsors.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description_en', models.TextField(max_length=2048)),
                ('description_fr', models.TextField(max_length=2048)),
                ('logo', models.ImageField(upload_to=pycon.sponsors.models.Sponsor.upload_path, max_length=512)),
                ('logo_bw', models.ImageField(upload_to=pycon.sponsors.models.Sponsor.upload_path, max_length=512)),
                ('name', models.CharField(max_length=128)),
                ('level', models.CharField(max_length=64)),
                ('order', models.IntegerField(default=1)),
                ('twitter_en', models.CharField(blank=True, max_length=32)),
                ('twitter_fr', models.CharField(blank=True, max_length=32)),
                ('url_website_en', models.URLField(blank=True)),
                ('url_website_fr', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name_en', models.CharField(max_length=255)),
                ('name_fr', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='type',
            field=models.ForeignKey(to='sponsors.Type'),
        ),
    ]
