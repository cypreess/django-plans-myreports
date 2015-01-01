# Create your views here.
from django.conf import settings
from django.views.generic import View, ListView
from plans.models import Invoice


class InvoiceView(ListView):

    template_name = 'plans_reports/invoices.html'

    def get_queryset(self):
        return Invoice.invoices.filter(issued__year=self.kwargs['year'], issued__month=self.kwargs['month']).order_by('number')

    def get_context_data(self, **kwargs):
        context = super(InvoiceView, self).get_context_data(**kwargs)
        context['logo_url'] = getattr(settings, 'PLANS_INVOICE_LOGO_URL', None)
        return context


