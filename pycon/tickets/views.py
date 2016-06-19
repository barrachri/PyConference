from weasyprint import HTML, CSS

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import select_template
from django.template import RequestContext

from pycon.core.views import PyconTemplateView

from pycon.schedule.models import Day, Proposal
from pycon.schedule.timetable import TimeTable


class ScheduleView(PyconTemplateView):
    template_name = 'schedule/schedule.html'

    def get(self, request):
        days_qs = Day.objects.all()
        days = [TimeTable(day) for day in days_qs]

        return self.render_to_response({
            'days': days
        })


class PresentationView(PyconTemplateView):
    template_name = 'schedule/presentation.html'

    def get(self, request, pk, *args, **kwargs):
        proposal = get_object_or_404(Proposal, pk=pk)

        return self.render_to_response({
            'p': proposal
        })

class InvoiceView(PyconTemplateView):
    template_name = 'tickets/invoice.html'

    def get(self, request, pk, *args, **kwargs):
        #invoice = get_object_or_404(Proposal, pk=pk)
        html_template = select_template(self.get_template_names())
        #user = request.user
        rendered_html = html_template.render(RequestContext(request, {})).encode(encoding="UTF-8")
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice_{}.pdf"'.format("EP2016#00125")
        #pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT +  'css/report.css')])
        pdf_file = HTML(string=rendered_html).write_pdf(response)

        return response
