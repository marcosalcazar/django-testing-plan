# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Requirement'
        db.create_table(u'testing_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'testing', ['Requirement'])

        # Adding model 'TestCase'
        db.create_table(u'testing_testcase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('objective', self.gf('django.db.models.fields.TextField')()),
            ('test_case_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['testing.Requirement'])),
            ('execution_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('estimated_execution_time', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'testing', ['TestCase'])

        # Adding model 'TestCasePreCondition'
        db.create_table(u'testing_testcaseprecondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(related_name='preconditions', to=orm['testing.TestCase'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'testing', ['TestCasePreCondition'])

        # Adding model 'TestCasePostCondition'
        db.create_table(u'testing_testcasepostcondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postconditions', to=orm['testing.TestCase'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'testing', ['TestCasePostCondition'])

        # Adding model 'TestCaseRevision'
        db.create_table(u'testing_testcaserevision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(related_name='revisions', to=orm['testing.TestCase'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'testing', ['TestCaseRevision'])

        # Adding model 'TestCaseStep'
        db.create_table(u'testing_testcasestep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['testing.TestCase'])),
            ('step_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('step_action', self.gf('django.db.models.fields.TextField')()),
            ('step_expected_result', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'testing', ['TestCaseStep'])

        # Adding model 'TestCaseCorrectiveAction'
        db.create_table(u'testing_testcasecorrectiveaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(related_name='corrective_actions', to=orm['testing.TestCase'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'testing', ['TestCaseCorrectiveAction'])


    def backwards(self, orm):
        # Deleting model 'Requirement'
        db.delete_table(u'testing_requirement')

        # Deleting model 'TestCase'
        db.delete_table(u'testing_testcase')

        # Deleting model 'TestCasePreCondition'
        db.delete_table(u'testing_testcaseprecondition')

        # Deleting model 'TestCasePostCondition'
        db.delete_table(u'testing_testcasepostcondition')

        # Deleting model 'TestCaseRevision'
        db.delete_table(u'testing_testcaserevision')

        # Deleting model 'TestCaseStep'
        db.delete_table(u'testing_testcasestep')

        # Deleting model 'TestCaseCorrectiveAction'
        db.delete_table(u'testing_testcasecorrectiveaction')


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
        u'testing.requirement': {
            'Meta': {'object_name': 'Requirement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'testing.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'estimated_execution_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'execution_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.TextField', [], {}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['testing.Requirement']"}),
            'test_case_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'testing.testcasecorrectiveaction': {
            'Meta': {'object_name': 'TestCaseCorrectiveAction'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corrective_actions'", 'to': u"orm['testing.TestCase']"})
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
        u'testing.testcasestep': {
            'Meta': {'object_name': 'TestCaseStep'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step_action': ('django.db.models.fields.TextField', [], {}),
            'step_expected_result': ('django.db.models.fields.TextField', [], {}),
            'step_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': u"orm['testing.TestCase']"})
        }
    }

    complete_apps = ['testing']