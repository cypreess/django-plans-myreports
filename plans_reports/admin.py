from django.contrib import admin
from plans_reports.models import NonInvoicedReport, NonInvoicedReportElement, InvoicedReport, InvoicedReportElement


class InvoicedReportElementInline(admin.TabularInline):
    model = InvoicedReportElement
    extra = 1


class InvoicedReportAdmin(admin.ModelAdmin):
    inlines = (InvoicedReportElementInline,)
    list_display = ('__unicode__', 'created')

admin.site.register(InvoicedReport, InvoicedReportAdmin)


class NonInvoicedReportElementInline(admin.TabularInline):
    model = NonInvoicedReportElement
    extra = 1


class NonInvoicedReportAdmin(admin.ModelAdmin):
    inlines = (NonInvoicedReportElementInline,)
    list_display = ('__unicode__', 'created')

admin.site.register(NonInvoicedReport, NonInvoicedReportAdmin)
