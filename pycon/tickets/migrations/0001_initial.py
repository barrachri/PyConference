# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_auto_20160618_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=2)),
                ('start_validity', models.DateField(null=True)),
                ('end_validity', models.DateField(null=True)),
                ('recipient_type', models.CharField(choices=[('c', 'Company'), ('s', 'Student'), ('p', 'Personal')], max_length=1, default='p')),
                ('ticket_type', models.CharField(choices=[('conference', 'Conference ticket'), ('partner', 'Partner Program'), ('event', 'Event'), ('other', 'Other')], max_length=10, db_index=True, default='conference')),
                ('payment_type', models.CharField(choices=[('p', 'Payment'), ('v', 'Voucher'), ('d', 'Deposit')], max_length=1, default='p')),
                ('blob', models.TextField(blank=True)),
                ('conference', models.ForeignKey(to='schedule.Conference', related_name='fares')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='fare',
            unique_together=set([('conference', 'code')]),
        ),
    ]
