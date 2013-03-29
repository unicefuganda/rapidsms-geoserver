# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PollData.total'
        db.add_column('geoserver_polldata', 'total',
                      self.gf('django.db.models.fields.FloatField')(default=0, max_length=5, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PollData.total'
        db.delete_column('geoserver_polldata', 'total')


    models = {
        'geoserver.basicclasslayer': {
            'Meta': {'unique_together': "(('deployment_id', 'layer_id', 'district'),)", 'object_name': 'BasicClassLayer'},
            'deployment_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'style_class': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'geoserver.emisattendencedata': {
            'Meta': {'object_name': 'EmisAttendenceData'},
            'boys': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'female_teachers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'girls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_teachers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'total_pupils': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_teachers': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'geoserver.pollcategorydata': {
            'Meta': {'unique_together': "(('deployment_id', 'poll_id', 'district'),)", 'object_name': 'PollCategoryData'},
            'deployment_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll_id': ('django.db.models.fields.IntegerField', [], {}),
            'top_category': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'geoserver.polldata': {
            'Meta': {'unique_together': "(('deployment_id', 'poll_id', 'district'),)", 'object_name': 'PollData'},
            'deployment_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'poll_id': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'total_no': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'total_uncategorized': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'total_unknown': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'total_yes': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'uncategorized': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'unknown': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'yes': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'geoserver.pollresponsedata': {
            'Meta': {'unique_together': "(('deployment_id', 'poll_id', 'district'),)", 'object_name': 'PollResponseData'},
            'deployment_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'poll_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['geoserver']