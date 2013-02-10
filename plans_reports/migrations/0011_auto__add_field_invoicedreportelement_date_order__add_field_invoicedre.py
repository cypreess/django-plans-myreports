# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'InvoicedReportElement.date_order'
        db.add_column('plans_reports_invoicedreportelement', 'date_order',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InvoicedReportElement.description'
        db.add_column('plans_reports_invoicedreportelement', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'InvoicedReportElement.date_order'
        db.delete_column('plans_reports_invoicedreportelement', 'date_order')

        # Deleting field 'InvoicedReportElement.description'
        db.delete_column('plans_reports_invoicedreportelement', 'description')


    models = {
        'plans_reports.invoicedreport': {
            'Meta': {'ordering': "('-date', '-created')", 'object_name': 'InvoicedReport'},
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
            'date_order': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_sell': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans_reports.InvoicedReport']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
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