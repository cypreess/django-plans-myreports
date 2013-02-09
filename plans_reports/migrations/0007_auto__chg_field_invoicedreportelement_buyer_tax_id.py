# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'InvoicedReportElement.buyer_tax_id'
        db.alter_column('plans_reports_invoicedreportelement', 'buyer_tax_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'InvoicedReportElement.buyer_tax_id'
        raise RuntimeError("Cannot reverse this migration. 'InvoicedReportElement.buyer_tax_id' and its values cannot be restored.")

    models = {
        'plans_reports.invoicedreport': {
            'Meta': {'object_name': 'InvoicedReport'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'plans_reports.invoicedreportelement': {
            'Meta': {'ordering': "('sequence',)", 'object_name': 'InvoicedReportElement'},
            'buyer': ('django.db.models.fields.TextField', [], {}),
            'buyer_tax_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.DateField', [], {}),
            'date_sell': ('django.db.models.fields.DateField', [], {}),
            'global_sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans_reports.InvoicedReport']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tax_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'total_net': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        },
        'plans_reports.noninvoicedreport': {
            'Meta': {'object_name': 'NonInvoicedReport'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
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