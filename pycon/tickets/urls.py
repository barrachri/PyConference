from django.conf.urls import url
from pycon.tickets.views import ScheduleView, PresentationView, InvoiceView

urlpatterns = [
    url(
        regex = r"^$",
        view = ScheduleView.as_view(),
        name = 'schedule'
    ),
    url(
        regex = r"^(?P<pk>[0-9]+)/$",
        view = PresentationView.as_view(),
        name = 'schedule_presentation_detail'
    ),
    url(
        regex = r"^invoices/(?P<pk>[0-9]+)/$",
        view = InvoiceView.as_view(),
        name = 'schedule_presentation_detail'
    ),
]
