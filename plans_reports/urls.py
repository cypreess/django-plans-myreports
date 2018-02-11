from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from plans_reports.models import NonInvoicedReport, InvoicedReport
from plans_reports.views import InvoiceView

urlpatterns = patterns('',
    url(r'^noninvoiced/(?P<pk>\d+)/$', staff_member_required(DetailView.as_view(model=NonInvoicedReport)), name='plans_raport_noninvoiced'),
    url(r'^invoiced/(?P<pk>\d+)/$', staff_member_required(DetailView.as_view(model=InvoicedReport)), name='plans_raport_invoiced'),
    url(r'^invoiced/(?P<pk>\d+)/csv/$', staff_member_required(DetailView.as_view(model=InvoicedReport, template_name='plans_reports/invoicedreports_detail.csv')), name='plans_raport_invoiced_csv'),
    url(r'^invoices/(?P<year>\d+)/(?P<month>\d+)/$', staff_member_required(InvoiceView.as_view()), name='plans_raport_invoices'),


    )
