# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename 'corrective_action' field to 'description'
        db.rename_column('testing_testcasestate', 'corrective_action', 'description')

    def backwards(self, orm):
        # Rename 'description' field to 'corrective_action'
        db.rename_column('testing_testcasestate', 'description', 'corrective_action')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'requirements.requirement': {
            'Meta': {'object_name': 'Requirement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'testing.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'estimated_execution_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'execution_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.TextField', [], {}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'test_cases'", 'to': u"orm['requirements.Requirement']"}),
            'test_case_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'testing.testcasepostcondition': {
            'Meta': {'object_name': 'TestCasePostCondition'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postconditions'", 'to': u"orm['testing.TestCase']"})
        },
        u'testing.testcaseprecondition': {
            'Meta': {'object_name': 'TestCasePreCondition'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'preconditions'", 'to': u"orm['testing.TestCase']"})
        },
        u'testing.testcaserevision': {
            'Meta': {'object_name': 'TestCaseRevision'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['testing.TestCase']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'testing.testcasestate': {
            'Meta': {'object_name': 'TestCaseState'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'states_completed'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'states'", 'to': u"orm['testing.TestCase']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'states_verified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'testing.testcasestep': {
            'Meta': {'ordering': "['step_number']", 'object_name': 'TestCaseStep'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step_action': ('django.db.models.fields.TextField', [], {}),
            'step_expected_result': ('django.db.models.fields.TextField', [], {}),
            'step_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': u"orm['testing.TestCase']"})
        }
    }

    complete_apps = ['testing']