# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PuffText'
        db.create_table('sitemanager_pufftext', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser_safe.fields.FileBrowseField')(max_length=255, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('sitemanager', ['PuffText'])


    def backwards(self, orm):
        # Deleting model 'PuffText'
        db.delete_table('sitemanager_pufftext')


    models = {
        'sitemanager.pufftext': {
            'Meta': {'object_name': 'PuffText'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser_safe.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sitemanager']