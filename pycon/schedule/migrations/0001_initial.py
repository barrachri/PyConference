# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('photo', models.ImageField(upload_to='speaker_photos', blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(unique=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('proposal_id', models.PositiveIntegerField(unique=True, verbose_name='Proposal ID')),
                ('cancelled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['slot'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('day', models.ForeignKey(to='schedule.Day', related_name='sessions')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('content_override', models.TextField(blank=True)),
                ('day', models.ForeignKey(to='schedule.Day')),
            ],
            options={
                'ordering': ['day', 'start', 'end'],
            },
        ),
        migrations.CreateModel(
            name='SlotKind',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SlotRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('room', models.ManyToManyField(to='schedule.Room')),
                ('slot', models.ForeignKey(to='schedule.Slot')),
            ],
            options={
                'ordering': ['slot', 'room__order'],
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('bio', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('photo', models.ImageField(upload_to='speaker_photos', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='slot',
            name='kind',
            field=models.ForeignKey(to='schedule.SlotKind'),
        ),
        migrations.AddField(
            model_name='session',
            name='slots',
            field=models.ManyToManyField(to='schedule.Slot', related_name='sessions'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='additional_speakers',
            field=models.ManyToManyField(to='schedule.Speaker', blank=True, related_name='copresentations'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='slot',
            field=models.OneToOneField(null=True, blank=True, related_name='content_ptr', to='schedule.Slot'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='speaker',
            field=models.ForeignKey(to='schedule.Speaker', related_name='presentations'),
        ),
    ]
