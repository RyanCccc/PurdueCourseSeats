# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'used_book_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('seller_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('seller_contact', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'used_book', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'used_book_book')


    models = {
        u'used_book.book': {
            'Meta': {'object_name': 'Book'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'seller_contact': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'seller_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['used_book']