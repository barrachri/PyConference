# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=20, null=True, unique=True)),
                ('emit_date', models.DateField()),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('note', models.TextField(blank=True, help_text="Testo libero da riportare in fattura; posto al termine delle righe d'ordine riporta di solito gli estremi di legge")),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_url', models.TextField(blank=True)),
                ('complete', models.BooleanField(default=False)),
                ('billing_notes', models.TextField(blank=True)),
                ('card_name', models.CharField(verbose_name='Card name', max_length=200)),
                ('vat_number', models.CharField(blank=True, max_length=22, verbose_name='Vat Number')),
                ('cf_code', models.CharField(blank=True, max_length=16, verbose_name='Codice Fiscale')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Address')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='fare',
            name='end_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fare',
            name='start_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fare',
            name='vat',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='fare',
            field=models.ForeignKey(to='tickets.Fare'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(to='tickets.Order', related_name='order_items'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.OneToOneField(to='tickets.Order', related_name='invoices'),
        ),
    ]
