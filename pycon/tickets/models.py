"""
This is the model for the fares, tickets and invoice for the conference
"""

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext as _

# You import settings to access the settings_conference.py
from django.conf import settings

from pycon.schedule.models import Conference


class Fare(models.Model):
    '''
    Fare models
    '''
    conference = models.ForeignKey(Conference, related_name="fares")
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    start_validity = models.DateField(null=True, blank=True)
    end_validity = models.DateField(null=True, blank=True)
    recipient_type = models.CharField(max_length=1, choices=settings.FARE_TYPES, default='p')
    ticket_type = models.CharField(max_length=10, choices=settings.FARE_TICKET_TYPES, default='conference', db_index=True)
    payment_type = models.CharField(max_length=1, choices=settings.FARE_PAYMENT_TYPE, default='p')
    blob = models.TextField(blank=True)

    class Meta:
        unique_together = (('conference', 'code'),)

    def __str__(self):
        return '%s - %s' % (self.code, self.conference)

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.start_validity is not None and self.end_validity is not None:
            if self.start_validity > self.end_validity:
                raise ValidationError({'end_validity': _('End validity should be greater than start validity')})

class OrderManager(models.Manager):
    def create_order(self, *args, **kwargs):
        order = self.create(*args, **kwargs)
        # also create the order_items
        return order

    def save_order(self, *args, **kwargs):
        pass

class Order(models.Model):
    """
    The idea is to create first the order
    after the order is complete=True you should create the tickets
    """
    code = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(User, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    payment_url = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    billing_notes = models.TextField(blank=True)
    # Questi dati vengono copiati dallo User al fine di storicizzarli
    card_name = models.CharField(_('Card name'), max_length=200)
    vat_number = models.CharField(_('Vat Number'), max_length=22, blank=True)
    cf_code = models.CharField('Codice Fiscale', max_length=16, blank=True)
    # la country deve essere null perché un ordine può essere creato via admin
    # e in quel caso non è detto che si conosca
    #country = models.ForeignKey(Country, verbose_name=_('Country'), null=True)
    address = models.CharField(_('Address'), max_length=150, blank=True)

    objects = OrderManager()

    def __str__(self):
        if self.code:
            return ' #%s - %s' % (self.code, self.user.email)
        else:
            return 'Invoice id:%d' % self.id

class OrderItem(models.Model):
    fare = models.ForeignKey(Fare)
    order = models.ForeignKey(Order, related_name='order_items')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "%s (%s) - %s" % (self.order, self.fare, self.price)

class Invoice(models.Model):
    order = models.OneToOneField(Order, related_name='invoices')
    code = models.CharField(max_length=20, null=True, unique=True)
    emit_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # indica il tipo di regime iva associato alla fattura perche vengono
    # generate più fatture per ogni ordine contente orderitems con diverso
    # regime fiscale
    #vat = models.ForeignKey(Vat)

    note = models.TextField(
        blank=True,
        help_text='''Testo libero da riportare in fattura; posto al termine delle righe d'ordine riporta di solito gli estremi di legge''')

    def __str__(self):
        if self.code:
            return ' #%s' % self.code
        else:
            return 'Invoice id:%d' % self.id

    def invoice_items(self):
        return self.order.orderitem_set.filter(vat=self.vat) \
                                  .values('code','description') \
                                  .annotate(price=models.Sum('price'), count=models.Count('price')) \
                                  .order_by('-price')

    def vat_value(self):
        return self.price - self.net_price()

    def net_price(self):
        return self.price / (1 + self.vat.value / 100)
