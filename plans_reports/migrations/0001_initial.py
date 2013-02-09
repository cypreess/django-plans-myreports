# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InvoicedReport'
        db.create_table('plans_reports_invoicedreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('plans_reports', ['InvoicedReport'])

        # Adding model 'NonInvoicedReport'
        db.create_table('plans_reports_noninvoicedreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('issuer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('plans_reports', ['NonInvoicedReport'])


    def backwards(self, orm):
        # Deleting model 'InvoicedReport'
        db.delete_table('plans_reports_invoicedreport')

        # Deleting model 'NonInvoicedReport'
        db.delete_table('plans_reports_noninvoicedreport')


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
        }
    }

    complete_apps = ['plans_reports']