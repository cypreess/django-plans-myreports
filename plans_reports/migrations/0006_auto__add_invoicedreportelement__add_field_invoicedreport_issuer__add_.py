# -*- coding: utf-8 -*-
import datetime
from pytz import utc
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InvoicedReportElement'
        db.create_table('plans_reports_invoicedreportelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans_reports.InvoicedReport'])),
            ('global_sequence', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('invoice_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_issued', self.gf('django.db.models.fields.DateField')()),
            ('date_sell', self.gf('django.db.models.fields.DateField')()),
            ('buyer', self.gf('django.db.models.fields.TextField')()),
            ('buyer_tax_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_net', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('tax_total', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
        ))
        db.send_create_signal('plans_reports', ['InvoicedReportElement'])

        # Adding field 'InvoicedReport.issuer'
        db.add_column('plans_reports_invoicedreport', 'issuer',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'InvoicedReport.created'
        db.add_column('plans_reports_invoicedreport', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow().replace(tzinfo=utc), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'InvoicedReportElement'
        db.delete_table('plans_reports_invoicedreportelement')

        # Deleting field 'InvoicedReport.issuer'
        db.delete_column('plans_reports_invoicedreport', 'issuer')

        # Deleting field 'InvoicedReport.created'
        db.delete_column('plans_reports_invoicedreport', 'created')


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
            'buyer_tax_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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