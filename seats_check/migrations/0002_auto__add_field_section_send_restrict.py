# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Section.send_restrict'
        db.add_column(u'seats_check_section', 'send_restrict',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Section.send_restrict'
        db.delete_column(u'seats_check_section', 'send_restrict')


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
            'send_restrict': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['seats_check']