# coding=utf-8
import calendar
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.db.models import Sum, Max
from pytz import utc, timezone
from plans.models import Order, Invoice


class InvoicedReport(models.Model):
    date = models.DateField()
    issuer = models.TextField(blank=True)
    created = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('-date', '-created')

    def elements(self):
        return InvoicedReportElement.objects.filter(report=self, non_invoiced=False)

    def elements_non_invoiced(self):
        return InvoicedReportElement.objects.filter(report=self, non_invoiced=True)

    def total_netto(self):
        return self.elements().exclude(tax=None).aggregate(Sum('total_net'))['total_net__sum']

    def tax_total(self):
        return self.elements().aggregate(Sum('tax_total'))['tax_total__sum']

    def total_netto_np(self):
        return self.elements().filter(tax=None).aggregate(Sum('total_net'))['total_net__sum']

    def total(self):
        return self.elements().aggregate(Sum('total'))['total__sum']

    def save(self, force_insert=False, force_update=False, using=None):


        if not self.issuer:
            issuer = settings.PLANS_INVOICE_ISSUER
            self.issuer = u"%s\n%s\n%s %s\n%s" % (
                issuer['issuer_name'],
                issuer['issuer_street'],
                issuer['issuer_zipcode'],
                issuer['issuer_city'],
                issuer['issuer_tax_number'],
            )

        if not self.created:
            self.created = datetime.utcnow().replace(tzinfo=utc)

        create = False
        if self.pk is None:
            create = True
        response = super(InvoicedReport, self).save(force_insert, force_update, using)
        if create or force_insert:
            self.make_report()
        return response


    def make_report(self):
        site_name = Site.objects.get_current().name
        seq = 1
        seq_non_invoiced = 1

        bulk_elements = []

        for invoice in Invoice.invoices.filter(issued__year=self.date.year, issued__month=self.date.month).order_by('number').select_related('order'):

            non_invoiced = False
            current_seq = seq
            if invoice.issued.year != invoice.selling_date.year or invoice.issued.month != invoice.selling_date.month:
                non_invoiced = True
                current_seq = seq_non_invoiced



            bulk_elements.append(InvoicedReportElement(
                report = self,
                sequence = current_seq,
                group = site_name,
                invoice_number = invoice.full_number,
                date_issued = invoice.issued,
                date_sell = invoice.selling_date,
                buyer = u"%s, %s, %s %s, %s" % (invoice.buyer_name, invoice.buyer_street, invoice.buyer_zipcode, invoice.buyer_city, invoice.buyer_country),
                buyer_tax_id = invoice.buyer_tax_number,
                total = invoice.total,
                total_net = invoice.total_net,
                tax_total = invoice.tax_total,
                tax = invoice.tax,

                date_order = invoice.order.completed,
                description = u"%s, zamówienie #%d" % (site_name, invoice.order.id),
                non_invoiced = non_invoiced,

            ))
            if non_invoiced:
                seq_non_invoiced += 1
            else:
                seq += 1

        InvoicedReportElement.objects.bulk_create(bulk_elements)

    def __unicode__(self):
        return u"Rejestr faktur VAT z miesiąca " + unicode(self.date.strftime('%Y-%m'))

    def get_absolute_url(self):
        return reverse('plans_raport_invoiced', kwargs={'pk': self.pk})

class InvoicedReportElement(models.Model):
    report = models.ForeignKey(InvoicedReport)
    sequence = models.IntegerField(db_index=True)
    invoice_number = models.CharField(max_length=50)
    group = models.TextField()

    date_order = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    date_issued = models.DateField()
    date_sell = models.DateField()
    buyer = models.TextField()
    buyer_tax_id = models.CharField(max_length=50, blank=True, null=True)
    total_net = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    tax_total = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2, db_index=True, null=True,
                              blank=True) # Tax=None is whet tax is not applicable

    non_invoiced = models.BooleanField(default=False)

    class Meta:
        ordering = ('sequence', )




class NonInvoicedReport(models.Model):
    date = models.DateField()
    issuer = models.TextField(blank=True)
    created = models.DateTimeField(blank=True)

    def __unicode__(self):
        return u"Sprzedaż nieewidencjonowana z miesiąca " + unicode(self.date.strftime('%Y-%m'))

    def get_absolute_url(self):
        return reverse('plans_raport_noninvoiced', kwargs={'pk': self.pk})


    def elements(self):
        return NonInvoicedReportElement.objects.filter(report=self)

    def total(self):
        return NonInvoicedReportElement.objects.filter(report=self).aggregate(Sum('total'))['total__sum']

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.issuer:
            issuer = settings.PLANS_INVOICE_ISSUER
            self.issuer = u"%s\n%s\n%s %s\n%s" % (
                issuer['issuer_name'],
                issuer['issuer_street'],
                issuer['issuer_zipcode'],
                issuer['issuer_city'],
                issuer['issuer_tax_number'],
            )

        if not self.created:
            self.created = datetime.utcnow().replace(tzinfo=utc)

        create = False
        if self.pk is None:
            create = True
        response = super(NonInvoicedReport, self).save(force_insert, force_update, using)
        if create or force_insert:
            self.make_report()
        return response


    def make_report(self):
        settingstime_zone = timezone(settings.TIME_ZONE)

        start = datetime(year=self.date.year, month=self.date.month, day=1).replace(tzinfo=settingstime_zone)
        end = (start + relativedelta(months=+1)).replace(tzinfo=settingstime_zone)

        site_name = Site.objects.get_current().name

        bulk_elements = []

        seq = 1
        for order in Order.objects.filter(status=Order.STATUS['COMPLETED'], completed__gte=start, completed__lt=end).prefetch_related('invoice_set').select_related('user').order_by('id'):
            if not filter(lambda i: i.type==Invoice.INVOICE_TYPES['INVOICE'] and i.issued.year == order.completed.year and i.issued.month == order.completed.month, order.invoice_set.all()):
                bulk_elements.append(NonInvoicedReportElement(report=self, sequence=seq, date=order.completed.date(), description=u"%s, zamówienie #%d, konto '%s', %s" % (site_name, order.id, order.user.username, order.user.email), total=order.total()))
                seq += 1

        NonInvoicedReportElement.objects.bulk_create(bulk_elements)

class NonInvoicedReportElement(models.Model):
    report = models.ForeignKey(NonInvoicedReport)
    sequence = models.IntegerField(db_index=True)
    date = models.DateField()
    description = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('sequence', )