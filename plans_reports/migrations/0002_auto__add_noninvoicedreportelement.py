# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NonInvoicedReportElement'
        db.create_table('plans_reports_noninvoicedreportelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('plans_reports', ['NonInvoicedReportElement'])


    def backwards(self, orm):
        # Deleting model 'NonInvoicedReportElement'
        db.delete_table('plans_reports_noninvoicedreportelement')


    models = {
        'plans_reports.invoicedreport': {
            'Meta': {'object_name': 'InvoicedReport'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'plans_reports.noninvoicedreport': {
            'Meta': {'object_name': 'NonInvoicedReport'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.TextField', [], {})
        },
        'plans_reports.noninvoicedreportelement': {
            'Meta': {'object_name': 'NonInvoicedReportElement'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['plans_reports']