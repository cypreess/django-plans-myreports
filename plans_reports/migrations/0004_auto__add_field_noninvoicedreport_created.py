# -*- coding: utf-8 -*-
import datetime
from pytz import utc
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NonInvoicedReport.created'
        db.add_column('plans_reports_noninvoicedreport', 'created',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.utcnow().replace(tzinfo=utc), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NonInvoicedReport.created'
        db.delete_column('plans_reports_noninvoicedreport', 'created')


    models = {
        'plans_reports.invoicedreport': {
            'Meta': {'object_name': 'InvoicedReport'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'plans_reports.noninvoicedreport': {
            'Meta': {'object_name': 'NonInvoicedReport'},
            'created': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'plans_reports.noninvoicedreportelement': {
            'Meta': {'ordering': "('sequence',)", 'object_name': 'NonInvoicedReportElement'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans_reports.NonInvoicedReport']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['plans_reports']