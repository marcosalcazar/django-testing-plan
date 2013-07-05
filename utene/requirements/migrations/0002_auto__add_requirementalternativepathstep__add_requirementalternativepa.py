# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequirementAlternativePathStep'
        db.create_table(u'requirements_requirementalternativepathstep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alternative_path', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.RequirementAlternativePath'])),
            ('step_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'requirements', ['RequirementAlternativePathStep'])

        # Adding model 'RequirementAlternativePath'
        db.create_table(u'requirements_requirementalternativepath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requirements.RequirementStep'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'requirements', ['RequirementAlternativePath'])

        # Adding model 'RequirementPostCondition'
        db.create_table(u'requirements_requirementpostcondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postconditions', to=orm['requirements.Requirement'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'requirements', ['RequirementPostCondition'])

        # Adding model 'RequirementRevision'
        db.create_table(u'requirements_requirementrevision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='revisions', to=orm['requirements.Requirement'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'requirements', ['RequirementRevision'])

        # Adding model 'RequirementStep'
        db.create_table(u'requirements_requirementstep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['requirements.Requirement'])),
            ('step_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'requirements', ['RequirementStep'])

        # Adding model 'RequirementPreCondition'
        db.create_table(u'requirements_requirementprecondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='preconditions', to=orm['requirements.Requirement'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'requirements', ['RequirementPreCondition'])

        # Adding field 'Requirement.objective'
        db.add_column(u'requirements_requirement', 'objective',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Requirement.responsible'
        db.add_column(u'requirements_requirement', 'responsible',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'RequirementAlternativePathStep'
        db.delete_table(u'requirements_requirementalternativepathstep')

        # Deleting model 'RequirementAlternativePath'
        db.delete_table(u'requirements_requirementalternativepath')

        # Deleting model 'RequirementPostCondition'
        db.delete_table(u'requirements_requirementpostcondition')

        # Deleting model 'RequirementRevision'
        db.delete_table(u'requirements_requirementrevision')

        # Deleting model 'RequirementStep'
        db.delete_table(u'requirements_requirementstep')

        # Deleting model 'RequirementPreCondition'
        db.delete_table(u'requirements_requirementprecondition')

        # Deleting field 'Requirement.objective'
        db.delete_column(u'requirements_requirement', 'objective')

        # Deleting field 'Requirement.responsible'
        db.delete_column(u'requirements_requirement', 'responsible_id')


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
            'objective': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'requirements.requirementalternativepath': {
            'Meta': {'object_name': 'RequirementAlternativePath'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.RequirementStep']"})
        },
        u'requirements.requirementalternativepathstep': {
            'Meta': {'object_name': 'RequirementAlternativePathStep'},
            'alternative_path': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requirements.RequirementAlternativePath']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'requirements.requirementpostcondition': {
            'Meta': {'object_name': 'RequirementPostCondition'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postconditions'", 'to': u"orm['requirements.Requirement']"})
        },
        u'requirements.requirementprecondition': {
            'Meta': {'object_name': 'RequirementPreCondition'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'preconditions'", 'to': u"orm['requirements.Requirement']"})
        },
        u'requirements.requirementrevision': {
            'Meta': {'object_name': 'RequirementRevision'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['requirements.Requirement']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'requirements.requirementstep': {
            'Meta': {'object_name': 'RequirementStep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': u"orm['requirements.Requirement']"}),
            'step_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['requirements']