# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BookTagShip'
        db.create_table(u'webooks_book_tag_ship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webooks.Book'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webooks.Tag'])),
        ))
        db.send_create_signal(u'webooks', ['BookTagShip'])

        # Adding model 'Tag'
        db.create_table(u'webooks_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'webooks', ['Tag'])

        # Adding field 'Chapter.number'
        db.add_column(u'webooks_chapter', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Book.name'
        db.alter_column(u'webooks_book', 'name', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Deleting model 'BookTagShip'
        db.delete_table(u'webooks_book_tag_ship')

        # Deleting model 'Tag'
        db.delete_table(u'webooks_tag')

        # Deleting field 'Chapter.number'
        db.delete_column(u'webooks_chapter', 'number')


        # Changing field 'Book.name'
        db.alter_column(u'webooks_book', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))

    models = {
        u'webooks.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'books'", 'to': u"orm['webooks.Tag']", 'through': u"orm['webooks.BookTagShip']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'webooks.booktagship': {
            'Meta': {'object_name': 'BookTagShip', 'db_table': "u'webooks_book_tag_ship'"},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webooks.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webooks.Tag']"})
        },
        u'webooks.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webooks.Book']"}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1048576'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'webooks.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['webooks']