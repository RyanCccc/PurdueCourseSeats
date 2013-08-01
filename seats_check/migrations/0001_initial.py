# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'seats_check_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crn', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('max_seats_num', self.gf('django.db.models.fields.IntegerField')()),
            ('current_seats_num', self.gf('django.db.models.fields.IntegerField')()),
            ('remain_seats_num', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'seats_check', ['Section'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'seats_check_section')


    models = {
        u'seats_check.section': {
            'Meta': {'object_name': 'Section'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'crn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'current_seats_num': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_seats_num': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'remain_seats_num': ('django.db.models.fields.IntegerField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['seats_check']