from django.contrib import admin
from pycon.tickets.models import *

class FareAdmin(admin.ModelAdmin):
    list_display = ('conference', 'code', 'name', 'description', 'start_validity', 'end_validity', 'ticket_type', 'price', 'vat')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created', 'complete')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('fare', 'order', 'price')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'code', 'emit_date', 'payment_date', 'price')

admin.site.register(Fare, FareAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
